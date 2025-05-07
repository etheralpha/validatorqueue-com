# validatorqueque-com

This repo contains the source code for the [ValidatorQueue.com](https://validatorqueque.com).

Provides an estimate of the waiting time before your Ethereum validator becomes active or eligible for exit.
The data is fetched using the [beaconcha.in API](https://beaconcha.in/api/v1/docs/index.html#/Validator/get_api_v1_validators_queue).

The data is updated every ~ 15min. The first reading of each UTC+0 day is recorded for historical data.

To execute/build locally:

1. Create virtual environment: `python3 -m venv venv/`
1. Start python virtual environment: `. venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Run the script: `python build.py`
1. Close virtual environment: `deactivate`
1. Or run the last 4 steps in one command: `. venv/bin/activate && pip install -r requirements.txt && python build.py && deactivate`


This project is maintained by [Ether Alpha](https://etheralpha.org/).
