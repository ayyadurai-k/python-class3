
"""
declared function with three variables
first checking a is greater b and c if true return a
second checking b is greater than a and c if true return b
third just return c as bug 
"""
def biggest_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


ans = biggest_of_three(10,14,30)

print("Answer : ",ans)