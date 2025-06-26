# Given a list of integers x, find the peak elements. A peak is an element that is greater than its neighbors.
#  Example: x = [1, 2, 3, 1, 10, 8]
#  Output: peaks = [3, 10]

numbers= [12, 2, 4, 19, 7, 35, 90, 32, 12, 44, 18]

def Fpeaks(x):
    peak = []
    n = len(x)
    
    for i in range(n):
        if i == 0:
            if n > 1 and x[i] > x[i + 1]:
                peak.append(x[i])
        elif i == n - 1:
            if x[i] > x[i - 1]:
                peak.append(x[i])
        else:
            if x[i] > x[i - 1] and x[i] > x[i + 1]:
                peak.append(x[i])
    
    return peak

print(Fpeaks(numbers))