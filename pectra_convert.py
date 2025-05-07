import json

# Load the original JSON data
with open('historical_data.json', 'r') as infile:
    data = json.load(infile)

# Update each object's 'entry_queue' and 'exit_queue' values
for item in data:
    if 'entry_queue' in item:
        item['entry_queue'] *= 32
    if 'exit_queue' in item:
        item['exit_queue'] *= 32

# Save the modified data to a new file
with open('historical_data_new.json', 'w') as outfile:
    json.dump(data, outfile, indent=None, separators=(',', ':'))

print("Updated data saved to historical_data_new.json")