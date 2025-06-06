import json

animal= {
    "Dog":"Serosh",
    "Cat": "Philly"
}
ser_animal= json.dumps(animal)
print("This is JSON serialization: ", json_animal)

des_animal= json.loads(json_animal)
print("This is JSON deserialization: ", des_animal)


# Serialization of python data types to JSON
# dict= object, list & tuple= array, str= string, int & float= number, None= null
# dict, list and tuples are not taken as JSON key

with open("create.json", "w") as file:  
    json.dump(animal, file)
    print("JSON file written.")
    
with open("indent.json", "w") as file:  
    json.dump(animal, file, indent= 3)
    print("JSON file written.")

with open("readingtest.json", "r") as file:
    print("\nReading JSON file: ")
    content= json.load(file)  
    # print(json.load(file)['Intern'])
    print(content['Daily Task'])
    
