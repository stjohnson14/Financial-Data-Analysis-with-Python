import os
import csv
import statistics

months = 0
net_total = 0
PL_change = []
average_change = 0
maxdate = []
mindate = []
previousmonth = 0
date = []

budget_csv = os.path.join('Pybank', 'Resources', 'budget_data.csv')
budget_csv_output = os.path.join('PyBank', 'Analysis', 'budget_output.txt')
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csvheader = next(csvreader)
    for i in csvreader:
        months += 1
        date.append(str(i[0]))
        net_total += int(i[1])
        PL_change.append(int(i[1]) - previousmonth)
        previousmonth = int(i[1])

print(f"CSV Header: {csvheader}")       
print(f"Months: {months}")
print(f"Net total is {net_total}")
print(f"Profit/Loss change: {PL_change}")

average_change = round(statistics.mean(PL_change))
maxdate = None
mindate= None

for i in PL_change:
     if i >= max(PL_change):
         maxdate = PL_change.index(i)
     if i <= min(PL_change):
         mindate = PL_change.index(i)

print(f"The average change is {average_change}")
print(f"The greatest increase in profits was {PL_change[25]} on {date[25]} ")
print(f"The greatest decrease was {PL_change[44]} on {date[44]}")

# output = (
#    f"\n Financial Analysis \n"
#    f"------------------------------\n"
#    f"Total Months: {months}\n"
#    f"Total: ${net_total}\n"
#    f"Average  Change: ${average_change}\n"
#    f"Greatest Increase in Profits: {date[25]} (${PL_change[25]})\n"
#    f"Greatest Decrease in Profits: {date[44]} (${PL_change[44]})\n")

with open(budget_csv_output, "w") as output_file:
    
    output_file.write("\n Financial Analysis \n")
    output_file.write("---------------------\n")
    output_file.write(f"Total Months: {months}\n") 
    output_file.write("---------------------\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average  Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {date[25]} (${PL_change[25]})\n")
    output_file.write(f"Greatest Decrease in Profits: {date[44]} (${PL_change[44]})\n")
  


