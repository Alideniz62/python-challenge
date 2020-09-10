#______________________PyBank__________________________

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

  # The total number of months included in the dataset

  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period



#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")
#print(csvpath)

# Open and read the CSV
with open(csvpath, newline="") as csvfile:
    #print(csvreader)
    
    # Read the header row and printing
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
 
    # Declare variables
    Dates = []
    Profit_Losses = []
    Value = []
    Increase_D = ""
    Decrease_D = ""
    
    
    for row in csvreader:
        Dates.append(row[0])
        Profit_Losses.append(int(row[1]))
      
    for i in range(1, len(Profit_Losses)):
        
        # Change between_months
        Value.append(Profit_Losses[i] - Profit_Losses[i-1])
        
        # Finding average
        Average_Change = sum(Value) / len(Value)
        
        # Greatest increase/decrease and date
        Greatest_Increase = max(Value)
        Increase_D = str(Dates[Value.index(max(Value))])
        
        Greatest_Decrease = min(Value)
        Decrease_D = str(Dates[Value.index(min(Value))])
        
    
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", len(Dates))
    print("Total: $", sum(Profit_Losses))
    print("Average Change: $", round(Average_Change,2))
    print("Greatest Increase: ", Increase_D, "($", Greatest_Increase,")")
    print("Greatest Decrease: ", Decrease_D, "($", Greatest_Decrease,")")
    
    pybank = open("pybank.txt", "w")

    text1 = "Financial Analysis"
    text2 = "---------------------"
    text3 = "Total Months: ", len(Dates)
    text4 = "Total: $", sum(Profit_Losses)
    text5 = "Average Change: $", round(Average_Change,2)
    text6 = "Greatest Increase: ", Increase_D, "($", Greatest_Increase,")"
    text7 = "Greatest Decrease: ", Decrease_D, "($", Greatest_Decrease,")"
    pybank.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(text1,text2,text3,text4,text5,text6,text7))
    
    
