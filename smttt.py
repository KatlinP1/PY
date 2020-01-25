
def difference(n): 
    if n <= 17:
        return 17-n 
    if n > 17:
        return abs(n-17)*2

print (difference (5))
print (difference (28))

def kitten (a,b,c):
    sum = a+b+c
    if a==b and b==c:
        return  3*sum 
    return sum 

y= kitten (3,3,3)
print (y)
