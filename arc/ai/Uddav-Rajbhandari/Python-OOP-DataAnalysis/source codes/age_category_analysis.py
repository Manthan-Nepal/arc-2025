import numpy as np
import pandas as pd


def input_from_user():
    """
    Function to take input from the user and store it in a dictionary.
    """
    dict = {"Name": [] ,
        "Roll": [],
        "Address": [],
        "Age": []
        }
    while True:
        name = input("Enter your name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        if not name.strip().isalpha():
            print("Invalid name. Please enter a valid name.")
            continue
        roll = input("Enter your roll number: ")
        address = input("Enter your address: ")
        if not address.strip():
            print("Invalid address. Please enter a non-empty value.")
            continue
        age = int(input("Enter your age: "))
        
        dict["Name"].append(name)
        dict["Roll"].append(roll)
        dict["Address"].append(address)
        dict["Age"].append(age)

    return dict

    
def create_dataframe(data_dict):
    df = pd.DataFrame(data_dict)
    return df

def categorize_age(df):
    fill_category = lambda x: 'Junior' if x <= 15 else ('Mid' if x > 15 and x<=25 else 'Senior')
    df['Category'] = df['Age'].apply(fill_category)

    return df

def display_dataframe(df):
    print("\nDataFrame with Age Categories:")
    print(df)
    
def calculate_average_and_mode(df):
    average_age = df['Age'].mean()
    mode_category = df['Category'].mode()[0]  # mode returns a Series, take the first value
    print(f"\nAverage Age: {average_age}")
    print(f"Most frequent category is : {mode_category}")



if __name__ == "__main__":
    data_dict = input_from_user()
    df = create_dataframe(data_dict)
    if df.empty:
        print("No data entered. Exiting.")
    else:
        df = categorize_age(df)
        display_dataframe(df)
        calculate_average_and_mode(df)

  