import os, csv

# File path
my_file = os.path.join("budget_data.csv")
# Set variables
net_total = months_count = change = greatest_increase = greatest_decrease = 0
greatest_increase_month = greatest_decrease_month = ""
data = []

# open the budget data file
with open(my_file, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    file_header = next(csvreader)

    for row in csvreader:
        # the total number of months included in the dataset
        months_count = months_count + 1

        # The net total amount of "Profit/Losses" over the entire period
        net_total = int(net_total) + int(row[1])

        # Put data into a list to calculate monthly change
        data.append(row)

        # Loop through the whole list and get the monthly change (next month - current month)
        # len -1 is for the avoiding inaccurate calculation for the last data
        for i in range(len(data) - 1):
            monthly_change = int((data)[i + 1][1]) - int((data)[i][1])

            # The greatest increase
            if greatest_increase < monthly_change:
                greatest_increase = monthly_change
                greatest_increase_month = data[i + 1][0]

            # The greatest decrease
            if greatest_decrease > monthly_change:
                greatest_decrease = monthly_change
                greatest_decrease_month = data[i + 1][0]

            # average
            average_val = round(
                (int((data)[-1][1]) - int((data)[0][1])) / (len(data) - 1), 2
            )


print(f"Months: {months_count}")
print(f"Total number of records: {net_total}")
print(f"Average : {average_val}")
print(f"Greatest Increase: {greatest_increase_month} ({greatest_increase})")
print(f"Greatest Decrease: {greatest_decrease_month} ({greatest_decrease})")
