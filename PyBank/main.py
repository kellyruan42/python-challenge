# Dependencies and Setup
import os
import csv
import statistics

# Open the csv
with open("./Resources/budget_data.csv", 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        # Skip the header
        next(reader)

        # Create empty lists and empty variables 
        rowcount = 0
        totalnet = 0
        budget_newdata = []
        monthly_change = []
        date = []

        # Create for loop for the date
        for row in reader:
            rowcount += 1
            totalnet += int(row[1])
            budget_newdata.append(int(row[1]))
            date.append(str(row[0]))

        # Create for loop to calculate
        for i in range(rowcount-1):
            change = budget_newdata[i+1] - budget_newdata[i]
            monthly_change.append(change)
        average_change = statistics.mean(monthly_change)
    
        # Put correct row number for the date
        best_row = monthly_change.index(max(monthly_change)) + 1
        worst_row = monthly_change.index(min(monthly_change)) + 1
    
        # Print the result
        print("Financial Analysis")
        print("---------------------------------------------------")
        print("Total Months:", rowcount) 
        print("Total: $", totalnet)
        print("Average Change: $", round(average_change, 2))
        print("Greatest Increase in Profits: " + date[best_row] + " ($" + str(max(monthly_change)) + ")")
        print("Greatest Dncrease in Profits: " + date[worst_row] + " ($" + str(min(monthly_change)) + ")")

        # Export the output in txt
        f = open('Analysis and Output.txt', 'w')
        f.write("\nFinancial Analysis\n")
        f.write("\n---------------------------------------------------\n")
        f.write(f'\nTotal Months: {rowcount}\n')
        f.write(f'\nTotal: ${totalnet}\n')
        f.write(f'\nAverage Change: ${round(average_change, 2)}\n')
        f.write(f'\nGreatest Increase in Profits: {date[best_row]} (${str(max(monthly_change))})\n')
        f.write(f'\nGreatest Decrease in Profits: {date[worst_row]} (${str(min(monthly_change))})')
        f.close()