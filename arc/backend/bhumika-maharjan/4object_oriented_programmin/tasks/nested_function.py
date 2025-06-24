# Create a nested function and use nonlocal to modify a variable from the outer function.

def outer():
    msg = "hello"
    def nested():
        nonlocal msg
        msg ="hi"
        print(f"message inside nested {msg}")      

    nested()
    print(f"message in outer {msg}")
    return msg

outer()


