# Import os module
import os

# Import csv module for reading csv files
import csv
# Sets path for .csv data set file
csvpath = os.path.join('Resources', 'budget_data.csv')

# empty lists to store month strings and net change integers
netChangeList = []
collect_months = []

with open(csvpath) as csvfile:
    
# csvreader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
# read the header row first
    csv_header = next(csvreader)
    
    # set accumulators and variables to zero for counting rows and summing integers
    row_months = 0
    profitTotal = 0
    previousValue_row = 0
    currentValue = 0
    netChangeTotal = 0
# read each row of data after the header
    for row in csvreader:
    # set counters to increment and variable to grab second column integer    
        row_months = row_months + 1
        currentValue = int(row[1])
        profitTotal += currentValue
        # conditional to grab first row value to enable previousValue start at zero
        if row_months == 1:
            previousValue = currentValue

# used 'continue' statement to skip row and allow first row to become previous row
# 'continue' statement learning source: https://builtin.com/software-engineering-perspectives/pass-vs-continue-python          
            
            continue
        # store difference of profitLoss values and populate empty lists
        else:
            netChange = currentValue - previousValue
            netChangeTotal += netChange
            netChangeList.append(netChange)
            collect_months.append(row[0])
            previousValue = currentValue
            averageChange = sum(netChangeList)/len(netChangeList)
            roundAverageChange = round(averageChange,2)
        # max, min, and index used to store respective values in variables
            max_increase_netChange = max(netChangeList)
            max_increase_netChange_month = netChangeList.index(max_increase_netChange)
            max_increase_netChange_date = collect_months[max_increase_netChange_month]

            min_increase_netChange = min(netChangeList)
            min_increase_netChange_month = netChangeList.index(min_increase_netChange)
            min_increase_netChange_date = collect_months[min_increase_netChange_month]
# send nonformatted results to terminal
print("Financial Analysis\n\n")
print("---------------------\n\n")
print("Total Months: ", row_months,"\n")
print("Total: ","$",profitTotal,"\n")
print("Average Change: ","$",roundAverageChange,"\n")
print("Greatest Increase in Profits: ",max_increase_netChange_date,"$",max_increase_netChange,"\n")
print("Greatest Decrease in Profits: ",min_increase_netChange_date,"$",min_increase_netChange,"\n")
# set location for output text file 
output_path = os.path.join("analysis", "budget_data_output.txt")
with open(output_path, 'w') as textfile:
# send formatted results to text file
    textfile.write("Financial Analysis\n\n")
    textfile.write("---------------------\n\n")
    textfile.write(f"Total Months:  {row_months} \n")
    textfile.write(f"Total: $ {profitTotal} \n")
    textfile.write(f"Average Change: ${roundAverageChange}\n")
    textfile.write(f"Greatest Increase in Profits: {max_increase_netChange_date} ${max_increase_netChange}\n")
    textfile.write(f"Greatest Decrease in Profits: {min_increase_netChange_date} ${min_increase_netChange}\n")






       


