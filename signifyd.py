import csv
import datetime as dt
import sys

emails = {}

def process_file(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # Example code: You can parse the date from a record with:
            date = dt.datetime.strptime(row[0], "%Y-%m-%d")
            ids = row[1]
            status = row[2] 
            if ids not in emails:
                emails[ids] = []
                emails[ids].append([date,status]) 
                if status == "PURCHASE": 
                    print(f"{date.date()},{ids},NO_HISTORY")
            else:
                good_history = 0
                unconfirmed_history = 0
                fraud_history = 0
                if status == "PURCHASE":
                    for reports in emails[ids]:
                        if reports[1] == "FRAUD_REPORT":
                            fraud_history += 1
                        else:
                            if (date - reports[0]).days > 90: 
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
    if len(sys.argv) != 2:
        print("Expecting a singular file argument.")
    else:
        process_file(sys.argv[1])