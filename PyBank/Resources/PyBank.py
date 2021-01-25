

# Python Homework - Py Me Up, Charlie  - PyBank

# Import Modules/Dependencies
import os
import csv

# Variables
month = 0
amount = 0
change = []
month_count = []
increase = 0
increase_month = 0
decrease = 0
decrease_month = 0

# Set Path For File
PyBankPath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

# Open & Read CSV File
with open(PyBankPath, newline='') as csvfile:

    # CSV Reader Specifies Delimiter & Variable That Holds Contents
    PyBankReader = csv.reader(csvfile, delimiter=',')
    csv_header = next(PyBankReader)
    row = next(PyBankReader)

    # Calculate Total Number Of Months, Net Amount Of "Profit/Losses" & Set Variables For Rows
    previous_row = int(row[1])
    month += 1
    amount += int(row[1])
    increase = int(row[1])
    increase_month = row[0]

    # Read Each Row Of Data After The Header
    for row in PyBankReader:

        # Calculate Total Number Of Months Included In Dataset
        month += 1
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Period
        amount += int(row[1])

        # Calculate Change From Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        # Calculate The Greatest Increase
        if int(row[1]) > increase:
            increase = int(row[1])
            increase_month = row[0]

        # Calculate The Greatest Decrease
        if int(row[1]) < decrease:
            decrease = int(row[1])
            decrease_month = row[0]

    # Calculate The Average & The Date
    average_change = sum(change) / len(change)

    highest = max(change)
    lowest = min(change)

# Print Analysis
print(f"Financial Analysis")
print(f"--------Done by JAG-------------------")
print(f"Total Months: {month}")
print(f"Total: ${amount}")
print(f"Average Change: ${average_change:.2f}")
print(
    f"Greatest Increase in Profits:, {increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {decrease_month}, (${lowest})")

print(f"-----------------------------------------")

# Specify File To Write To
output_file = os.path.join('.', 'PyBank', 'Resources',
                           'budget_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

    # Write New Data in the text file
    # #TODO Take a screenshot for readme File

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"--------Done by JAG -------------------\n")
    txtfile.write(f"Total Months: {month}\n")
    txtfile.write(f"Total: ${amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(
        f"Greatest Increase in Profits:, {increase_month}, (${highest})\n")
    txtfile.write(
        f"Greatest Decrease in Profits:, {decrease_month}, (${lowest})\n")
    txtfile.write(f"---------------------------\n")
