# Import os module
import os

# Import csv module for reading csv files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
data = []
profitLoss = []
profitTotal = []
netChangeList = []
currentValue = []
previousValue = []
currentValueList = []
collect_months = []
analysis = zip(data, profitLoss)
with open(csvpath) as csvfile:
    
# csvreader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
# read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #previousValue = 0
    row_months = 0
    profitTotal = 0
    previousValue_row = 0
    currentValue = 0
   #averageChange = 0
    netChangeTotal = 0
# read each row of data after the header
    for row in csvreader:
        
        row_months = row_months + 1
        currentValue = int(row[1])
        profitTotal += currentValue
        
        if row_months == 1:
            previousValue = currentValue
            continue
        else:
            netChange = currentValue - previousValue
            netChangeTotal += netChange
            netChangeList.append(netChange)
            collect_months.append(row[0])
            previousValue = currentValue
            averageChange = sum(netChangeList)/len(netChangeList)
            roundAverageChange = round(averageChange,2)
            
            max_increase_netChange = max(netChangeList)
            max_increase_netChange_month = netChangeList.index(max_increase_netChange)
            max_increase_netChange_date = collect_months[max_increase_netChange_month]

            min_increase_netChange = min(netChangeList)
            min_increase_netChange_month = netChangeList.index(min_increase_netChange)
            min_increase_netChange_date = collect_months[min_increase_netChange_month]
print("Financial Analysis\n\n")
print("---------------------\n\n")
print("Total Months: ", row_months,"\n")
print("Total: ","$",profitTotal,"\n")
print("Average Change: ","$",roundAverageChange,"\n")
print("Greatest Increase in Profits: ",max_increase_netChange_date,"$",max_increase_netChange,"\n")
print("Greatest Decrease in Profits: ",min_increase_netChange_date,"$",min_increase_netChange,"\n")

output_path = os.path.join("analysis", "budget_data_output.txt")
with open(output_path, 'w') as textfile:

    textfile.write("Financial Analysis\n\n")
    textfile.write("---------------------\n\n")
    textfile.write(f"Total Months:  {row_months} \n")
    textfile.write(f"Total: $ {profitTotal} \n")
    textfile.write(f"Average Change: ${roundAverageChange}\n")
    textfile.write(f"Greatest Increase in Profits: {max_increase_netChange_date} ${max_increase_netChange}\n")
    textfile.write(f"Greatest Decrease in Profits: {min_increase_netChange_date} ${min_increase_netChange}\n")





#def total(months):
    # set up accumulator (running total)
    #total = 0
    # use a loop to loop throught the list of values
    #for n in months:
        #total += n
    #return total





       


