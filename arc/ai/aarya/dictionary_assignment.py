import pandas as pd

dict={
    "name":[],
    "roll":[],
    "age":[],
    "address":[]
}

def collect_data():
    for i in range(10):
        print(f"Enter details for student {i+1}")
        name = input("Enter your name: ")
        roll = input("Enter your roll: ")
        age = input("Enter your age: ")
        address = input("Enter your address: ")

        dict["name"].append(name)
        dict["roll"].append(int(roll))
        dict["age"].append(int(age))
        dict["address"].append(address)

collect_data()  #function call to take input and add to dictionary

df = pd.DataFrame(dict) #converts dictionary into dataframe

def assign_category(age):
    if age <= 15:
        return 'Junior'
    elif 15 < age <= 25:
        return 'Mid'
    else:
        return 'Senior'

df['category'] = df['age'].apply(assign_category)

print("Dataframe: ")
print(df)

average_age = df['age'].mean()
most_frequent_category = df['category'].mode()

print(f"The average age is: {average_age: .2f}")
print(f"Most frequent category based on age is: {most_frequent_category}")


