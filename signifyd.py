import csv
import datetime as dt
import sys

emails = {}

def process_file(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # Example code: You can parse the date from a record with:
            date = dt.datetime.strptime(row[0], "%Y-%m-%d") # strptime reformat to year/month/day
            ids = row[1] #first column is email
            status = row[2] #second column is status
            if ids not in emails:
                emails[ids] = []
                emails[ids].append([date,status]) #this adds new users
                if status == "PURCHASE": 
                    print(f"{date.date()},{ids},NO_HISTORY") 
            else:
                good_history = 0
                unconfirmed_history = 0
                fraud_history = 0
                if status == "PURCHASE":
                    for reports in emails[ids]:
                        if reports[1] == "FRAUD_REPORT": #reports[1] is the second part, date
                            fraud_history += 1
                        else:
                            if (date - reports[0]).days > 90: #checks more than 90 days, report[0] is the date
                                good_history += 1
                            else:
                                unconfirmed_history += 1
                    if fraud_history > 0:
                        print(f"{date.date()},{ids},FRAUD_HISTORY:{fraud_history}")
                    elif good_history > 0:
                        print(f"{date.date()},{ids},GOOD_HISTORY:{good_history}")
                    else:
                        print(f"{date.date()},{ids},UNCONFIRMED_HISTORY:{unconfirmed_history}")
                emails[ids].append([date,status]) 

if __name__ == "__main__":
    if len(sys.argv) != 2: #if the length of the argument is at least two files 'signifyd.py signifydtest'
        print("Expecting a singular file argument.")
    else:
        process_file(sys.argv[1])

'''
improve this: 
    only works when the input is sorted because it assumes the input is in 
    chronological order bc the list used to sort the status of the user
    - new entries are in the back of the list

time complexity:
n^2
- slow, loops through for each individual entries, it has to compare against all previous entires
- will be slow if n is very large
- for each input, it checks whether or not in the list, then if not it goes to check for history
- also loops through previous ones to add that value


Company value:
curious and hungry
tenacious: very big problem, try to break it down into smaller parts that I can understand and go from there
'''