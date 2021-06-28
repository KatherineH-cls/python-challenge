
# Homework for Bootcamp module 3

# read in accounting data from csv file and perform financial analysis

import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    #print(f"csvheader: {csv_header}")

    count_months = 0
    total_profit = 0
    max_profit = 0
    max_loss = 0
    change_profit = []
    #profit_data = []
    month = []
    profit = []
    sum_change = 0
    max_change_pos = 0
    max_change_neg = 0

    # read in profit data and count the total number of rows
    for row in csvreader:
        count_months+=1
        total_profit += float(row[1])
        
        # find max profit and loss
        if float(row[1]) > 0:
            if float(row[1]) > max_profit:
                max_profit = float(row[1])
        elif float(row[1]) <0:
            if float(row[1]) < max_loss:
                max_loss = float(row[1])

       
        # create lists of months and profit
        month.append(row[0])
        profit.append(float(row[1]))

    
    for i in range(1,count_months):
        change_profit.append((profit[i]-profit[i-1]))
        sum_change += (profit[i]-profit[i-1])

    avg_change = round((sum_change / (count_months - 1)),2)   

    for j in range(count_months-1):
    # find max positive and negative change
        if change_profit[j] > 0:
            if change_profit[j] > max_change_pos:
                max_change_pos = change_profit[j]
                max_pos_index = j
        elif change_profit[j] <0:
            if change_profit[j] < max_change_neg:
                max_change_neg = change_profit[j]
                max_neg_index = j

    max_pos_month = month[max_pos_index + 1]
    max_neg_month = month[max_neg_index + 1]
    
    print("")
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: ${int(total_profit)}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {max_pos_month}  (${int(max_change_pos)})")
    print(f"Greatest Decrease in Profits: {max_neg_month}  (${int(max_change_neg)})")
    print("")

# Specify the file to write to
output_path = os.path.join("analysis", "financial_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text:

    
    
    text.write("Financial Analysis")
    text.write("\n")
    text.write("-------------------------------")
    text.write("\n")
    text.write(f"Total Months: {count_months}")
    text.write("\n")
    text.write(f"Total: ${int(total_profit)}")
    text.write("\n")
    text.write(f"Average Change: ${avg_change}")
    text.write("\n")
    text.write(f"Greatest Increase in Profits: {max_pos_month}  (${int(max_change_pos)})")
    text.write("\n")
    text.write(f"Greatest Decrease in Profits: {max_neg_month}  (${int(max_change_neg)})")
    
    
