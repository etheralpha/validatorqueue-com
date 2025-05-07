import requests
import os
import math
import time
import json
from datetime import datetime, timezone
from partials.head import head
from partials.dark_mode_toggle import dark_mode_toggle
from partials.toast import toast
from partials.header import header
from partials.overview import overview
from partials.faq import faq
from partials.churn_schedule import churn_schedule
from partials.historical_charts import historical_charts
from partials.footer import footer


queue_endpoint = "https://beaconcha.in/api/v1/validators/queue"
queue_data = requests.get(queue_endpoint).json()["data"]
epoch_endpoint = "https://mainnet.beaconcha.in/api/v1/epoch/finalized"
epoch_data = requests.get(epoch_endpoint).json()["data"]
apr_endpoint = "https://beaconcha.in/api/v1/ethstore/latest"
apr_data = requests.get(apr_endpoint).json()["data"]
supply_endpoint = "https://ultrasound.money/api/v2/fees/supply-over-time"
supply_data = requests.get(supply_endpoint).json()

current_time = time.time()


def estimate_entry_waiting_time():
	beaconchain_entering = round(queue_data["beaconchain_entering"])
	active_validators = queue_data["validatorscount"]
	entry_waiting_time, entry_waiting_time_days, entry_churn, entry_churn_time_days = calculate_wait_time(active_validators, beaconchain_entering, "entry")
	print("\nbeaconchain_entering: \n\t" + str(beaconchain_entering))
	print("\nentry_waiting_time: \n\t" + str(entry_waiting_time))
	print("\nentry_waiting_time_days: \n\t" + str(entry_waiting_time_days))
	return entry_waiting_time, entry_waiting_time_days, beaconchain_entering, active_validators, entry_churn


def estimate_exit_waiting_time():
	beaconchain_exiting = round(queue_data["beaconchain_exiting"])
	active_validators = queue_data["validatorscount"]
	exit_waiting_time, exit_waiting_time_days, exit_churn, exit_churn_time_days = calculate_wait_time(active_validators, beaconchain_exiting, "exit")
	print("\nbeaconchain_exiting: \n\t" + str(beaconchain_exiting))
	print("\nexit_waiting_time: \n\t" + str(exit_waiting_time))
	print("\nexit_waiting_time_days: \n\t" + str(exit_waiting_time_days))
	return exit_waiting_time, exit_waiting_time_days, beaconchain_exiting, exit_churn


def network_data():
	eth_supply = round(supply_data["d1"][0]["supply"])
	print("\neth_supply: \n\t" + str(eth_supply))
	amount_eth_staked = round(epoch_data["votedether"]/1000000000)
	print("\namount_eth_staked: \n\t" + str(amount_eth_staked))
	percent_eth_staked = round(amount_eth_staked/eth_supply * 10000)/100
	print("\npercent_eth_staked: \n\t" + str(percent_eth_staked))
	staking_apr = round(apr_data["avgapr7d"] * 10000)/100
	print("\nstaking_apr: \n\t" + str(staking_apr))

	return eth_supply, amount_eth_staked, percent_eth_staked, staking_apr


def calculate_wait_time(active_validators, queue, type):
	epoch_churn = 256
	entry_churn = 256
	exit_churn = 256
	if type == "entry":
		epoch_churn = entry_churn
	if type == "exit":
		epoch_churn = exit_churn
	slot_time = 12
	slots_per_epoch = 32
	epoch_seconds = slot_time * slots_per_epoch
	daily_churn = (86400 / epoch_seconds) * epoch_churn
	churn_time_days = 0
	
	if queue > 0:
		churn_time_days = queue / daily_churn

	print("\nepoch_seconds: \n\t" + str(epoch_seconds))
	print("\ndaily_churn: \n\t" + str(daily_churn))
	print("\nchurn_time_days: \n\t" + str(churn_time_days))
	print("\nepoch_churn: \n\t" + str(epoch_churn))

	waiting_time_seconds = round(churn_time_days * 86400)

	waiting_time_months = math.floor(waiting_time_seconds // 2592000)
	waiting_time_months_days = round( (waiting_time_seconds % 2592000)/2592000*30 )

	waiting_time_days = math.floor(waiting_time_seconds // 86400)
	waiting_time_days_hours = round( (waiting_time_seconds % 86400)/86400*24 )

	waiting_time_hours = math.floor(waiting_time_seconds // 3600)
	waiting_time_hours_minutes = round( (waiting_time_seconds % 3600)/3600*60 )

	waiting_time_days_raw = waiting_time_seconds / 86400

	# if waiting_time_months > 0:
	#   months_text = "months"
	#   days_text = "days"
	#   if waiting_time_months == 1:
	#       months_text = "month"
	#   if waiting_time_months_days == 1:
	#       days_text = "day"
	#   formatted_wait_time = f"""{waiting_time_months} {months_text}, {waiting_time_months_days} {days_text}"""
	if waiting_time_days > 0:
		days_text = "days"
		hours_text = "hours"
		if waiting_time_days == 1:
			days_text = "day"
		if waiting_time_days_hours == 1:
			hours_text = "hour"
		formatted_wait_time = f"""{waiting_time_days} {days_text}, {waiting_time_days_hours} {hours_text}"""
	elif waiting_time_hours > 0:
		hours_text = "hours"
		minutes_text = "minutes"
		if waiting_time_hours == 1:
			hours_text = "hour"
		if waiting_time_hours_minutes == 1:
			minutes_text = "minute"
		formatted_wait_time = f"""{waiting_time_hours} {hours_text}, {waiting_time_hours_minutes} {minutes_text}"""
	else:
		minutes_text = "minutes"
		if waiting_time_hours_minutes == 1:
			minutes_text = "minute"
		formatted_wait_time = f"""{waiting_time_hours_minutes} {minutes_text}"""


	return formatted_wait_time, waiting_time_days_raw, epoch_churn, churn_time_days


def update_historical_data(entry_churn, exit_churn):
	with open('historical_data.json', 'r') as f:
		all_data = json.load(f)
		date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
		todays_data =  {
			"date":date,
			"validators":active_validators,
			"entry_queue":beaconchain_entering,
			"entry_wait":round(entry_waiting_time_days*100)/100,
			"exit_queue":beaconchain_exiting,
			"exit_wait":round(exit_waiting_time_days*100)/100,
			"current_entry_churn":entry_churn,
			"current_exit_churn":exit_churn,
			"ave_entry_churn":entry_churn,
			"ave_exit_churn":exit_churn,
			"supply":eth_supply,
			"staked_amount":amount_eth_staked,
			"staked_percent":percent_eth_staked,
			"apr":staking_apr
		}
		# print("\nhistorical_data: \n\t" + str(all_data))
		print("\ntodays_data: \n\t" + str(todays_data))
		if len(all_data) > 0 and all_data[-1].get('date') is not None:
			if date != all_data[-1]['date']:
				all_data.append(todays_data)
				with open('historical_data.json', 'w') as f:
					json.dump(all_data, f, indent=None, separators=(',', ':'))
				f.close()
				print("historical data has been updated")
			else:
				print("historical data for the current date was already recorded")
		return all_data
					

def generate_html(entry_waiting_time, beaconchain_entering, exit_waiting_time, beaconchain_exiting, active_validators, entry_churn, exit_churn, amount_eth_staked, percent_eth_staked, staking_apr, historical_data):
	html_content = f"""<!DOCTYPE html>
		<html lang="en">
		{head}
		<body>
			{dark_mode_toggle}
			{toast()}
			<div class="container">
				{header(current_time)}
				{overview(entry_waiting_time, beaconchain_entering, exit_waiting_time, beaconchain_exiting, entry_churn, exit_churn, active_validators, amount_eth_staked, percent_eth_staked, staking_apr)}
				{faq}
				{churn_schedule(queue_data["validatorscount"])}
				{historical_charts}
				{footer(historical_data)}
			</div>
		</body>
		</html>"""

	with open("public/index.html", "w") as f:
		f.write(html_content)


entry_waiting_time, entry_waiting_time_days, beaconchain_entering, active_validators, entry_churn = estimate_entry_waiting_time()
exit_waiting_time, exit_waiting_time_days, beaconchain_exiting, exit_churn = estimate_exit_waiting_time()
eth_supply, amount_eth_staked, percent_eth_staked, staking_apr = network_data()
historical_data = update_historical_data(entry_churn, exit_churn)

generate_html(entry_waiting_time, beaconchain_entering, exit_waiting_time, beaconchain_exiting, active_validators, entry_churn, exit_churn, amount_eth_staked, percent_eth_staked, staking_apr, historical_data)
