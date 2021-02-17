'''
Given a string s containing only digits, return all possible valid IP addresses that can be obtained 
from s. You can return them in any order. A valid IP address consists of exactly four integers, each 
integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, 
"0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and 
"192.168@1.1" are invalid IP addresses. 
'''

def is_valid(ip):
    ip = ip.split(".") 
    for i in ip: #checking corner cases
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True
  
def convert(s): #converts string to IP address
    sz = len(s)
  
    if sz > 12: #checks string size
        return []
    snew = s
    l = []

    for i in range(1, sz - 2): #generates different combos
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]
                  
                if is_valid(snew): #makes sure valid combo
                    l.append(snew)
                snew = s
    return l 
  
A = "25525511135"
B = "25505011535"
print('A: ',convert(A))
print('B: ',convert(B))
