def average(*num):
    if num:
        return sum(num)/len(num)
    
print(average(1,2,3,4))