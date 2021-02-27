'''
pseudo idea:

user input numbers
have an empty array, we'll call 'res'
inputed numbers are sorted
check through numbers (whether or not prime)
if not prime
    break
else
    append to res 

in res
    sort so it is in decreasing order
    return first number without repeating value (thats our monomial)

'''

print('enter numbers (separate by commas) : ') #allow user to input numbers
res = []
num = [int(x) for x in input().split(",")] 
num.sort(reverse=True) #sort increasing order
 
for n in num: 
	for x in range(2,n//2): #check through each number
		if n//x==0: 
			break 
	else: 
        #res.append(n)
        print("largest prime from user input",n)
		break
    
monomial = #find the largest monomial
print('largest monomial from user input: ',monomial)

