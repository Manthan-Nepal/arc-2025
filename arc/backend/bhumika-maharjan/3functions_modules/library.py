import datetime
import random
import json

# datetime
now = datetime.datetime.now()
print("Current time:", now)

# random
random_number = random.randint(1, 10)
print("Random number:", random_number)

# json
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
print("JSON string:", json_str)

parsed_data = json.loads(json_str)
print("Parsed data:", parsed_data)
