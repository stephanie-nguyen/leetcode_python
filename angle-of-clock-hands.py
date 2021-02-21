'''
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
'''

def calcAngle(hour, minute):
    if (hour<0 or hour>12 or minute<0 or minute>60):
        return("enter valid time")
    if (hour == 12):
        hour = 0
    if (minute == 60):
        minute = 0
        
    minute_angle = (360/60)*minute
    hour_angle = (360/12)*hour + (minute/60)*(360/12)
    difference = abs(minute_angle-hour_angle)
    return min(difference, 360-difference)

hour = 7
minute = 34
print(calcAngle(hour,minute))

