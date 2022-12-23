import csv
import statistics


with open('/Users/kelly/Desktop/python-challenge/PyBank/Resources/budget_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    csv_reader = next(reader)

    rowcount = 0
    totalnet = 0
    budget_newdata = []
    monthly_change = []
    date = []
    for row in reader:
        rowcount += 1
        totalnet += int(row[1])
        budget_newdata.append(int(row[1]))
        date.append(str(row[0]))

    for i in range(rowcount-1):
        change = budget_newdata[i+1] - budget_newdata[i]
        monthly_change.append(change)
    average_change = statistics.mean(monthly_change)
    
    best_row = monthly_change.index(max(monthly_change)) + 1
    worst_row = monthly_change.index(min(monthly_change)) + 1
    
    print("Financial Analysis")
    print("---------------------------------------------------")
    print("Total Months:", rowcount) 
    print("Total: $", totalnet)
    print("Average Change: $", round(average_change, 2))
    print("Greatest Increase in Profits: " + date[best_row] + " ($" + str(max(monthly_change)) + ")")
    print("Greatest Dncrease in Profits: " + date[worst_row] + " ($" + str(min(monthly_change)) + ")")