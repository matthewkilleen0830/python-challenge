# Python Challenge:  PyBank

# Import required modules
import os
import csv

# Import optional and helpful module
import statistics as avg

# Set path to retrieve CSV file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Declare empty lists to store data from CSV
month = []
profit_or_loss = []
revenue_change = []

# Create function to find average of "revenue_change" list
def Average(myList):
    return(avg.mean(myList))

# Read CSV file using encoding for Windows and declare temporary variable to store contents
with open(budget_csv, newline='', encoding='utf-8') as csvfile:

    # Declare new variable specifying delimiter to separate values and store contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store and bypass the header row
    column_labels = next(csvreader)

    # Loop through each each row of data after the header in "csvreader" and add values to "month" list and to "profit_or_loss" list respectively
    for budget_row in csvreader:

        # Add month from each row to "month" list
        month.append(budget_row[0])

        # Cast profit or loss to number using 'float' and add to "profit_or_loss" list
        profit_or_loss.append(float(budget_row[1]))
    
# Declare variable, set initial value, and loop through values in "profit_or_loss" list to calculate total net profit or loss
net_profit = 0
for x in profit_or_loss:

    # Add next row's value to current row's value
    net_profit = x + net_profit

# Calculate difference in values between rows in "profit_or_loss" list and populate "revenue_change" list with month-to-month changes
revenue_change = [profit_or_loss[x + 1] - profit_or_loss[x] for x in range(0,len(profit_or_loss) - 1)]

# Declare variable, count total number of months, and store value
total_months = (len(month))

# Declare variable, recall previously defined function to calculate average of values in "revenue_change" list, and store value
average_change = Average(revenue_change)

# Declare variables, locate the greatest increase in profits (date and amount), and store values
greatest_profit = max(revenue_change)
list_max_profit = revenue_change.index(greatest_profit)
greatest_month = month[list_max_profit + 1]

# Declare variables, locate the least increase in profits (date and amount), and store values
least_profit = min(revenue_change)
list_min_profit = revenue_change.index(least_profit)
least_month = month[list_min_profit + 1]

# Declare variable, format numbered variables within f strings, store analysis summary, and print to terminal
analysis_summary =   (f'Financial Analysis\n'
                      f'---------------------------------------------------\n'
                      f'Total Months:  {total_months}\n'
                      f'Total:  ${net_profit:.0f}\n'
                      f'Average Change:  ${average_change:.2f}\n'
                      f'Greatest Increase in Profits:  {greatest_month} (${greatest_profit:.0f})\n'
                      f'Greatest Decrease in Profits:  {least_month} (${least_profit:.0f})')

print(analysis_summary)

# Write analysis summary to text file
analysis_output_file = os.path.join("Analysis", "PyBank_Financial_Analysis.txt")
with open(analysis_output_file, 'w') as textfile:
    textfile.write(analysis_summary)