'''
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
'''

def calcAngle(hour,minute): 
        if (hour < 0 or minute < 0 or hour > 12 or minute > 60): #check for valid time
            print('Enter valid time') 
          
        if (hour == 12): 
            hour = 0
        if (minute == 60): 
            minute = 0
          
        hour_angle = 0.5 * (hour * 60 + minute) #.5deg between those hour marks
        minute_angle = 6 * minute #6deg each min
          
        angle = abs(hour_angle - minute_angle) #12 is 0deg. find diff& angle btwn
        smallerangle = min(360 - angle, angle) #gives smaller angle being cut
        return smallerangle 

hour = 9
minute = 4
print(calcAngle(hour,minute), 'degrees') 
 
