# import sys
# sys.path.insert(1, 'D:\Programming\ARC_2025\arc-2025\arc\backend\salon-ngakhushi\python-data-structures\tasks')
# import file

# import sys
# sys.path.append('../')
# import ContactBook as modu

import contact_book_module as modu

print("\n", modu.ContactBook1.get("Name"))

print("\nSlicing: ", modu.ContactBook1["Name"][1:-1])

modu.ContactBook1["Name"].insert(2, 'Denji')
print("\n", modu.ContactBook1.get("Name"))

print("\nInitial Hiro: ", modu.ContactBook2.get("Hiro"))

modu.ContactBook2.update({"Hiro":{"phone": 9864234412, "email": "hiroyarika@yahoo.mail"}})
print("\nUpdated Hiro: ", modu.ContactBook2.get("Hiro"))