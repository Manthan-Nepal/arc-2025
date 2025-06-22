import pandas as pd

data={
    'name': [],
    'roll': [],     
    'address': [],
    'age': []
}

for i in range(1):
    print("Enter the details of student", i+1)
    name= input("Enter name: ")
    roll= input("Enter roll number: ")
    address= input("Enter address: ")
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input for age: {e}. Please enter a valid age.")

    data['name'].append(name)
    data['roll'].append(roll)
    data['address'].append(address)
    data['age'].append(age)

df=pd.DataFrame(data)

def assign_category(age):
    if age <= 15:
        return 'Junior'
    elif 15 < age <= 25:
        return 'Mid'
    else:
        return 'Senior'
    
df['category'] = df['age'].apply(assign_category)

# Step 5: Display the DataFrame
print("\nFinal DataFrame:\n")
print(df)

# Step 6: Calculate average age
average_age = df['age'].mean()
print(f"\nAverage Age: {average_age:.2f}")

# Step 7: Calculate most frequent category
most_frequent_category = df['category'].mode()[0]
print(f"Most Frequent Category: {most_frequent_category}")