'''
Given a Binary Tree, find count of distinct nodes in all the root to leaf paths and print the maximum. 
'''

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def largestUinquePathUtil(node, m):
    if (not node):
        return len(m)
    if node.data in m: #puts this nodes in hash
        m[node.data] += 1
    else:
        m[node.data] = 1
 
    max_path = max(largestUinquePathUtil(node.left, m),
                   largestUinquePathUtil(node.right, m))
 
    m[node.data] -= 1 #removes current node from path "hash"
   
    if (m[node.data] == 0): #if we reach the point where all duplicate values of current node is deleted
        del m[node.data]
    
    return max_path
 
def largestUinquePath(node): #finds long unique value path
    if (not node):
        return 0
 
    Hash = {} #stores all node values
 
    return largestUinquePathUtil(node, Hash) #returns max length unique value path
 
# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)
    root.right.right.right = newNode(9)
 
print(largestUinquePath(root))