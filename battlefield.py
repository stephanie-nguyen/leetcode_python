'''
John plays a game of battleships with his friend Sophia. The game is played on a square map of N rows, numbered from 1 to N.
Each row contains N cells, labeled with consecutive English upper-case letters ('A','B','C' etc). Each cell is identified
by a string composed of its row number followed by its column number: for example, "9C" denotes the third cell in the 9th 
row, and "15D" denotes teh fourth cell in the 15th row

John marks the position of all his ships on the map (which is not shown to Sonia). Ships are defined by rectangles with a 
maximum area of 4 cells. Sonia picks map cells to hit some ships. A ship is considered to be hit of at least one of its
constituent cells is hit. If all of a ship's cells are hit, the ship is sunk.

The goal is to count the number of sunk ships and the number of ships that have been hit but not sunk.

Examples:

1. Given N=4, S="1B 2C,2D 4D" and T="2B 2D 3D 4D 4A", your function should return "1,1"
2. Given N=3, S="1A 1B,2C 2C" and T="1B", your function should return "0,1". One ship was hit but not sunk. Note that the 
ship in cell 2C was not hit nor sunk, therefore it is not included in the result.
3. Given N=12, S="1A 2A,12A 12A" and T="12A", your function should return "1,0". One ship was sunk.

Assume that:
    1. N is an integer within the range [1 ... 26]
    2. String S containts the descriptions of rectangular ships of are not greater than 4 cells
    3. There can be at most one ship located on any map cell (ships do not overlap)
    4. Each map cell can appear in string T at most once
    5. String S and string T contains only valid positions given in a specified format
'''

import pdb

def solution(N,S,T):
    s = S.split(",")
    a = [] #all the coordinates of the ships
    sunk = 0
    hit = 0
    a_before = []
    a_after = []
    #print(s)
    for i in range(len(s)): # how many ships
        #pdb.set_trace()
        a.append([]) #creates new list for additional ships
        s[i] = s[i].split(" ") #1B 2C to ['1B', '2C']
        #print(s[i])
        if len(s[i][0]) < 3: #for 9x9 grids, checks for 1A....9? /s[i][0][1]
            #pdb.set_trace()
            if len(s[i][1]) > 2:
                pass
            else:
                for x in range(int(s[i][0][0]), int(s[i][1][0])+1): # range(beginning#, ending#)same ship
                    for y in range(ord(s[i][0][1]), ord(s[i][1][1])+1): #range() same as x in range, ord converts alphabet to number
                        a[i].append((str(x) + chr(y))) #create list of all squares for each ships location
        else: #for ships that use 10+ n boards, checks for 10A ... 26Z     
            for x in range(int(s[i][0][0])*10 + int(s[i][0][1]), int(s[i][1][0])*10 + int(s[i][1][1])+1):
                #print(int(s[i][0][0])*10 + int(s[i][0][1], int(s[i][1][0])*10) + int(s[i][1][1]+1)
                for y in range(ord(s[i][0][2]), ord(s[i][1][2])+1):
                    a[i].append((str(x) + chr(y)))
   
    t = T.split(" ") #converts string to list of all the coordinates of hits
    #pdb.set_trace()
    for x in a: #checks length of the ships
        a_before.append(len(x)) #a_before number of spots before any firing
    for x in t: #starts firing
        x = str(x)
        for y in a:
            if x in y:
                y.remove(x) #removed '2B'
                if not y: #empty list = ship has been sunk
                    sunk += 1
    #pdb.set_trace()
    for x in a: #number of the ships that are not hit yet
        a_after.append(len(x))
    for i in range(len(a_before)):
        if a_before[i] != a_after[i]:
            hit += 1 #counts how many ships have been hit

    hit = hit-sunk #removes ships sunken
    answer = f"{sunk},{hit}"
    return answer

N=4
S="1B 2C,10D 12D"
T="2B 2D 3D 4D 4A"
print(solution(N,S,T))