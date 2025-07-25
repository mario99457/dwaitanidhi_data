import json
import re

# Load the file
with open('gita/index.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update all "s" fields
for entry in data['data']:
    # Add danda after "उवाच" if not already present
    entry['s'] = re.sub(r'(उवाच)(?!।)', r'\1 ।\n', entry['s'])
    entry['s'] = re.sub(r'(श्री भगवानुवाच)(?!।)', r'\1 ।\n', entry['s'])
    entry['s'] = re.sub(r'\n\n', r'\n', entry['s'])

# Save to a new file
with open('gita/index_danda.txt', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated all 'uvacha' with danda in gita/index_danda.txt")