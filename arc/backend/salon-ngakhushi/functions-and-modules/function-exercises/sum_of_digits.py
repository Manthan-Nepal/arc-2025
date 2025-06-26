# Write a program to find the sum of digits in an integer.

def sum(x):
    sum= 0
    while x>0:
        sum += x%10
        x = x//10
    return sum

number= 1234
print("sum of digits: ", sum(number))