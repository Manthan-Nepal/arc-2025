fruits = ['watermelon', 'banana', 'stawberry', 'orange', 'banana']
print(fruits)

veg =["carrot", "broccoli", "spinach", "potato"]

merge =  fruits + veg
fruits.extend(veg)

unique_fruits = set(fruits)
print(unique_fruits)
unique_fruits.add('mango')       
unique_fruits.remove('banana')

fruit_list = list(unique_fruits)
print(fruit_list) 

fruit_list.append('kiwi')     
fruit_list.remove('orange')   
fruit_list.sort()  

fruit_tuple = tuple(fruit_list)
print(fruit_tuple)

person = {
    'name': 'Bhumika',
    'age': 30,
    'city': 'Kathmandu',
    'hobbies': ['traveling', 'baking']
}
print(person)
items = list(person.items())

print(items)
dictionary = dict(items)
print(dictionary)