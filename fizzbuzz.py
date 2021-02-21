'''
For a number divisible by 3, return 'fizz'
for a number divisible by 5, return 'buzz'
for a number divisible by both 3 and 5, return 'fizzbuzz'
'''

def fizzbuzz(n):
    for i in range(1,n):
        if i%3==0 and i%5==0:
            print(i,': fizzbuzz') 
        elif i % 5 == 0:
            print(i,': buzz') 
        elif i % 3 == 0:
            print(i,': fizz') 
        else:
            print(str(i))
    return fizzbuzz
n=15
print(fizzbuzz(n))