#The total number of months included in the dataset
import os
import csv
budget_csv = os.path.join("budget_data.csv")
#print("Working")
file = open(budget_csv)
numline = len(file.readlines())
print ("The total number of lines in" , int(numline - 1))

#The net total amount of "Profit/Losses" over the entire period
a = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    for row in csvreader:
        number = int(row[1])
        a.append(number)
       # sum = sum += row[1]
total = sum(a)
print("The Total is" ,total)
#The average of the changes in "Profit/Losses" over the entire period
def Average(x):
    print("The Average is" ,x/len(a))
Average(total)
#The greatest increase in profits (date and amount) over the entire period
def Max(x):
   max_num = max(a)
   print("The Max is" , max_num)
Max(total)

#The greatest decrease in losses (date and amount) over the entire period
def Min(x):
   min_num = min(a)
   print("The Min is" , min_num)
Min(total)
