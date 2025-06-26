# Create a nested function and use nonlocal to modify a variable from the outer function.

def superfunc():
    a= 67
    def subfunc():
        nonlocal a
        a= 12
        print("subfunc a: ", a)
        
    subfunc()
    print("superfunc a: ", a)
    
superfunc()