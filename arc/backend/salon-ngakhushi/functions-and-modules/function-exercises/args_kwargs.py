# Write a function that uses *args and **kwargs to print all passed values in formatted string example: Hello : name: "hari", roll:2, something like this.

def name(*names):
    j=0
    for i in names:
        print(f"My name is {i}, I am in my house.")
        j+=1
        

def kwnames(**names):
    for name, color in names.items():
        print(f"I am {name}, I like {color} color.")
        
name('red', 'bkue', 'green')
print(name())

kwnames(hiro= "red", siro= "blue", jiro= "green")
     

print(kwnames())