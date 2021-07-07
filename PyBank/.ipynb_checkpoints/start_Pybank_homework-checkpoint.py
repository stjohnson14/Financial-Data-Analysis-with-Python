import os
import csv
import statistics
# import pylance

# The dataset is composed of two columns: `Date` and `Profit/Losses`
# * Your task is to create a Python script that analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        # row - previous row = change --> change is added to average_total which is divided by months
#   * The greatest increase in profits (date and amount) over the entire period
            # if change is > change of previous row, this is new max_increase
            # if change is < change of previous row, this is new max_decrease
#   * The greatest decrease in profits (date and amount) over the entire period
# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

budget_csv = os.path.join('Pybank', 'Resources', 'budget_data.csv')
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    noheaders = csvreader.next()

    months = 0
    net_total = 0
    PL_change = []
    average_change = 0
    # previousmonth = None
    maxdate = []
    mindate = []

    for i in csvreader:
        months += 1
        net_total += int(i[1])
   
        let: 
            PL_change += int(i[1]) - int(i-1[1])
        
        

average_change = statistics.mean(PL_change)
# maxdate = None
# mindate= None

for i in PL_change:
    if i >= max(PL_change):
        maxdate = PL_change.index(i)
    if i <= min(PL_change):
        mindate = PL_change.index(i)


