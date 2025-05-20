import json


files = [
    'validators_2025_05_08.json',
    'validators_2025_05_09.json',
    'validators_2025_05_10.json',
    'validators_2025_05_11.json',
    'validators_2025_05_12.json',
    'validators_2025_05_13.json',
    'validators_2025_05_14.json',
    'validators_2025_05_15.json',
    'validators_2025_05_17.json',
    'validators_2025_05_18.json',
]

# schema exampe
# {
    # "execution_optimistic":false,
    # "finalized":false,
    # "data":[
    #     {
    #         "index":"0",
    #         "balance":"32017702117",
    #         "status":"active_ongoing",
    #         "validator": {
    #             "pubkey":"0x933ad9491b62059dd065b560d256d8957a8c402cc6e8d8ee7290ae11e8f7329267a8811c397529dac52ae1342ba58c95",
    #             "withdrawal_credentials":"0x0100000000000000000000000d369bb49efa5100fd3b86a9f828c55da04d2d50",
    #             "effective_balance":"32000000000",
    #             "slashed":false,
    #             "activation_eligibility_epoch":"0",
    #             "activation_epoch":"0",
    #             "exit_epoch":"18446744073709551615",
    #             "withdrawable_epoch":"18446744073709551615"
    #         }
    #     },
    #     ...
    # ]
# }

for file in files:
    with open(f"data/{file}", 'r') as infile:
        data = json.load(infile)
    overview = {
        'file': file,
        'validators': len(data['data']),
        '0x00': 0,
        '0x01': 0,
        '0x02': 0,
        '0x00_%': 0,
        '0x01_%': 0,
        '0x02_%': 0,
    }
    for item in data['data']:
        if '0x00' in item['validator']['withdrawal_credentials']:
            overview['0x00'] += 1
        if '0x01' in item['validator']['withdrawal_credentials']:
            overview['0x01'] += 1
        if '0x02' in item['validator']['withdrawal_credentials']:
            overview['0x02'] += 1
    overview['0x00_%'] = overview['0x00'] / overview['validators']
    overview['0x01_%'] = overview['0x01'] / overview['validators']
    overview['0x02_%'] = overview['0x02'] / overview['validators']
    print(overview)




