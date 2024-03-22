import os
import csv

#Creating our variables
total_months = 0
total_money = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
before_profit_or_loss = 0
total_profit_or_loss = 0
average_profit_or_loss = 0


#Opening our csv file 
csv_path = ("/Users/trevormcdonough/Downloads/Starter_Code-4/PyBank/Resources/budget_data.csv")

with open(csv_path) as csvfile: 
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    #Creating a for loop that'll run through each line in the file
    for line in csv_reader:
        profit_or_loss = int(line[1])
        total_months = total_months + 1
        total_money = total_money + profit_or_loss
        date = line[0]
        
        #Creating an if statement and another nested if statement that finds the greatest increase and decrease
        if total_months > 1:
            profit_change = profit_or_loss - before_profit_or_loss 
            total_profit_or_loss = total_profit_or_loss + profit_change
            if profit_change > greatest_increase[1]:
                greatest_increase = [date, profit_change]
            if profit_change < greatest_decrease[1]: 
                greatest_decrease = [date, profit_change]
        before_profit_or_loss = profit_or_loss


#Calculating the average profifs/losses throughout the file
average_profit_or_loss = (total_profit_or_loss / (total_months - 1))



#Printing out our final information
print("Financial Analysis")
print("-----------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_money}")
print(f"Average Change: ${average_profit_or_loss:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")



#Directing this informating into an output csv file to write on
output = r"/Users/trevormcdonough/Downloads/Starter_Code-4/PyBank/analysis/text.txt"

with open(output, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("---------------------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_money}\n")
    textfile.write(f"Average Change: ${average_profit_or_loss:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")