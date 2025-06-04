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


### Notes

- Due to a post-Pectra bug, entry/exit queue (ETH + time) from May 7, 2025 - May 21, 2025 is inaccurate and based on validators rather than balance. An approximate for the correct values can be made by multiplying those values by 32. In the future the data will be adjusted in this way and a note will be made here.
- On May 7, 2025 the queue data has shifted from validator-based to ETH-based. This change is not accounted for in the data.
- Due to a bug, historical conversion data is missing from 2025-05-21 through 2025-06-03 (including those dates as well).



This project is maintained by [hanniabu.eth](https://twitter.com/hanni_abu).
