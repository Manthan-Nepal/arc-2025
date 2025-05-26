"""2. Create an empty data dictionary with keys: name, roll, address, age where all the keys store a list of values. Fill in 10 valid data samples in the dictionary asking from the user. Then convert the dictionary to dataframe and add a new column to the dataframe called ‘category’. If the age is less than or equal to 15 then, category will be ‘Junior’, if its between 15 to 25(included), category will be ‘Mid’ and for the rest - category will be ‘Senior’. Display the dataframe. Calculate the average age and most frequent category.
"""
import pandas as pd

data = {
    "name": [],
    "roll": [],
    "address": [],
    "age": []
}

# for i in range(10):
#     print(f"\nEnter data for student {i + 1}:")
#     name = input("Name: ")
#     roll = input("Roll: ")
#     address = input("Address: ")

#     while True:
#         try:
#             age = int(input("Age: "))
#             break
#         except ValueError:
#             print("Invalid input. Please enter a valid age.")

#     data["name"].append(name)
#     data["roll"].append(roll)
#     data["address"].append(address)
#     data["age"].append(age)


data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jane"],
    "roll": ["R001", "R002", "R003", "R004", "R005", "R006", "R007", "R008", "R009", "R010"],
    "address": ["NY", "LA", "Chicago", "Houston", "Phoenix", "Seattle", "Denver", "Miami", "Boston", "Atlanta"],
    "age": [14, 16, 22, 28, 15, 19, 32, 13, 24, 26]
}


df = pd.DataFrame(data)


def category(age):
    if age <= 15:
        return "Junior"
    elif 15 < age <= 25:
        return "Mid"
    else:
        return "Senior"

df["category"] = df["age"].apply(category)

print("Final Dataframe:\n")
print(df)

average_age = df["age"].mean()
most_frequent_category = df["category"].mode()[0]

print(f"Average age: {average_age:.2f}")
print(f"Most frequent category: {most_frequent_category}")








