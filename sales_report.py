"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
"""
salespeople = [] #creating an empty list for salespeople
melons_sold = [] # creating an empty list for melons sold

f = open("sales-report.txt") # open the sales report file (do we need to do call .read() on it?)
for line in f: #for each line of the sales report, iterate through line by line
    line = line.rstrip() # strip each line of the unneccessary spaces at end
    entries = line.split("|") # split each line into individual strings at the pipe; creates a LIST
    salesperson = entries[0] # creating a variable salesperson, stores the name of salesperson
    melons = int(entries[2]) # creating a variable melons, converting to integer, stores num melons sold

    if salesperson in salespeople: # if salesperson is in the list of salespeople
        position = salespeople.index(salesperson) #the salesperson position is the index of where they are in list of salespeople
        melons_sold[position] += melons #if salesperson already in list, continue adding number of melons to get total melons sold per salesperson
    else:
        salespeople.append(salesperson) #if salesperson not already in list, add them to salespeople list
        melons_sold.append(melons) #same for melons


for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
"""
# Alternate solution

sales_perf = {} # create an empty dictionary
f = open("sales-report.txt")
for line in f:
    line = line.rstrip().split("|") # make each line a list of words
    salesperson = line[0]
    melons_sold = int(line[2])
    if salesperson not in sales_perf:
        sales_perf[salesperson] = melons_sold
    else:
        sales_perf[salesperson] += melons_sold

    print "{} sold {} melons".format(salesperson,melons_sold)
    
