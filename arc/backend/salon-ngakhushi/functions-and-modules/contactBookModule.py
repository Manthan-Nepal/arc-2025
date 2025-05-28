
ContactBook1= {}
ContactBook1["Name"]= ["Hiro", "Siro", "Yuro", "Jiro"]
ContactBook1["Phone"]= [385079483, 83645282, 9367384, 2363938]
ContactBook1["email"]= ["Hiro54@gmail.com", "siroheki@gmail.com", "yurayura@gmail.com", "jihiroyaku@yahoo.com"]

ContactBook2= {
    "Hiro": {"phone": 385079483, "email": "Hiro54@gmail.com"},
    "Siro": {"phone": 83645282, "email": "siroheki@gmail.com"},
    "Yuro": {"phone": 9367384, "email": "yurayura@gmail.com"},
    "Jiro": {"phone": 2363938, "email": "jihiroyaku@yahoo.com"}
}

def display():
    print("\n",ContactBook1["email"])
    print("\n",ContactBook2["Yuro"])