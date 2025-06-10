#local
def myfunc():
    x = 300
    print(x)

x=2
myfunc()


#global
g = 300
def myfunc():
    print(g)

myfunc()
print(g)


#both
b = 300

def myfunc():
  b = 200
  print(b)

myfunc()

print(b)


# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)