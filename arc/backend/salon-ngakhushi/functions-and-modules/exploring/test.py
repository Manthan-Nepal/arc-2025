def person(fname, *contact, **work):    
    print(f"Name: {fname}\nAddress: {contact[0]}\nEmail: {contact[1]}\nOther: {contact[2:]}")
    print(f"Worked as a {work.get('Office1')}.")
    print(f"Worked as a {work.get('Office2')}.")
    print(f"Worked as a {work.get('Office3')}.")
        
person('Serosh', 'kathmandu', 'ser0@gmail.com', 94737383,
       Office1= "Developer",
       Office2= "Engineer",
       Office3= "Analyst"
    )

# Default and Keyword arguments cannot be used with kwargs because they are read as kwargs instead.

# def person(fname, ID:int, *contact, **work):
#     print(f"ID No:{ID} Name: {fname}")
#     for i in contact:
#         print(f"Address: {contact[0]}\nEmail: {contact[1]\nOther: {contact}}")
#     for place, job in work.items():
#         print(f"Worked in {place} as a {job}.")
        
# person('Serosh', 'kathmandu', 'ser0@gmail.com',ID= 23,
#        Office1= "Developer",
#        Office2= "Engineer",
#        Office3= "Analyst"
#     )