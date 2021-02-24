'''
Given two integers X and Y, write a function which returns 
-1 if X < Y
0 if X == Y
+1 if X > Y
'''

def integers(x,y):
    if x<y:
        return -1
    elif x==y:
        return 0
    elif x>y:
        return 1
    return x,y

x=5
y=5
print(integers(x,y))