#import csv dependencies
import os
import csv

#read csv and make the path for file
data_output = os.path.join('/Users/haoonkim/Desktop/budget_data.csv')

#variables
total_month = 0
total_net = 0
previous_net = 0
change = 0
total_change = 0
greatest_increase = 0
grt_increase_month = 0
greatest_decrease = 0
grt_decrease_month = 0

#read data
with open(data_output, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the header first row
    csv_header = next(csvreader)
    
    #calculate data
    #count month and calculate net profit/loss
    #calculate change of months
    for row in csvreader:
        total_month += 1
        total_net += int(row[1])       
        if total_month > 1:
            change = int(row[1]) - previous_net
        total_change += change
        previous_net = int(row[1])
        
        #calculate greatest increase and decrease
        if change > greatest_increase:
            greatest_increase = change
            grt_increase_month = row[0]
       
        if change < greatest_decrease:
            greatest_decrease = change
            grt_decrease_month = row[0]
    #avg change of months    
    average_change = total_change/ (total_month - 1)

    #print financial analysis
    printout = (f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_month}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {grt_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {grt_decrease_month} (${greatest_decrease})")

print(printout)
