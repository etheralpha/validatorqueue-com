def overview(entry_waiting_time, beaconchain_entering, exit_waiting_time, beaconchain_exiting, entry_churn, exit_churn, active_validators, amount_eth_staked, percent_eth_staked, staking_apr):
	return f"""
		<div class="row row-cols-1 row-cols-md-2 gap-4 justify-content-center mx-1">

			<div class="card shadow border-light" style="max-width: 18rem;">
			  <div class="card-body">
			    <h5 class="card-title">Entry Queue</h5>
			    <div class="card-text">
			    	<div class="d-flex justify-content-between">
				    	<span>ETH: </span>
				    	<span>{"{:,}".format(beaconchain_entering)}</span>
			    	</div>
				    <div class="d-flex justify-content-between">
				    	<span>Wait: </span>
				    	<span>{entry_waiting_time}</span>
			    	</div>
			    	<div class="d-flex justify-content-between">
				    	<span>Churn: </span>
				    	<span>{entry_churn}/epoch</span>
			    	</div>
				</div>
			  </div>
			</div>

			<div class="card shadow border-light" style="max-width: 18rem;">
			  <div class="card-body">
			    <h5 class="card-title">Exit Queue</h5>
			    <div class="card-text">
			    	<div class="d-flex justify-content-between">
			    		<span>ETH: </span>
			    		<span>{"{:,}".format(beaconchain_exiting)}</span>
		    		</div>
				    <div class="d-flex justify-content-between">
				    	<span>Wait: </span>
				    	<span>{exit_waiting_time}</span>
			    	</div>
			    	<div class="d-flex justify-content-between">
				    	<span>
				    		Sweep Delay
				    		<a href="https://ethereum.org/en/staking/withdrawals#validator-sweeping" target="_blank" style="
							    text-decoration: none;
							    font-size: 12px;
							    position: relative;
							    top: -5px;">
							    ⓘ
						    </a>:
						</span>
				    	<span>{round(active_validators/115200, 1)} days</span>
			    	</div>
			    	<div class="d-flex justify-content-between">
				    	<span>Churn: </span>
				    	<span>{exit_churn}/epoch</span>
			    	</div>
				</div>
			  </div>
			</div>

			<div class="card shadow border-light" style="max-width: 18rem;">
			  <div class="card-body">
			    <h5 class="card-title">Consolidations</h5>
			    <div class="card-text">
			    	<div class="d-flex justify-content-between">
			    		<span>Pectrified: </span>
			    		<span><a href="https://pectrified.com/mainnet" target="_blank">Queues & Requests</a></span>
		    		</div>
				    <div class="d-flex justify-content-between">
				    	<span>Beaconcha.in: </span>
				    	<span><a href="https://light-mainnet.beaconcha.in/validators/el_consolidations" target="_blank">Requests</a></span>
			    	</div>
			    	<div class="d-flex justify-content-between">
				    	<span>Pectra.info: </span>
				    	<span><a href="https://www.pectra.info/consolidation" target="_blank">Rates by Entity</a></span>
			    	</div>
				</div>
			  </div>
			</div>

			<div class="card shadow border-light" style="max-width: 18rem;">
			  <div class="card-body">
			    <h5 class="card-title">Network</h5>
			    <div class="card-text">
			    	<div class="d-flex justify-content-between">
			    		<span>Active Validators: </span>
			    		<span>{"{:,}".format(active_validators)}</span>
		    		</div>
				    <div class="d-flex justify-content-between">
				    	<span>Staked ETH: </span>
				    	<span>{"{:,}".format(round(amount_eth_staked/100000)/10)}M ({percent_eth_staked}%)</span>
			    	</div>
			    	<div class="d-flex justify-content-between">
				    	<span>APR: </span>
				    	<span>{staking_apr}%</span>
			    	</div>
				</div>
			  </div>
			</div>

		</div>
		<div class="mt-3 mb-4 text-center">
			<a href="https://pectrified.com" target="_blank">Monitor Consolidations</a>
		</div>
	"""
