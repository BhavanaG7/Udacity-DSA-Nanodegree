"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#checking if calling number is from bangalore
def check_if_bangalore(lst):
    if lst[0][0:5]=="(080)":
        return True
    else:
        return False
    
#getting prfefix of called number    
def prefix_of_called_num(call):
    called_num=call[1]
    
    # Fixed lines
    if called_num[:2]=="(0":
        close_pos=called_num.index(")")
        return called_num[0:close_pos+1]
    
    #Telemarketers
    elif called_num[:3]=='140':
        return called_num[:3]
    
    #mobile number
    else:
        return called_num[:4]

#main
bangalore_called_prefix=[]
for call in calls:
    if check_if_bangalore(call):
        #getting all prefix code
        bangalore_called_prefix.append(prefix_of_called_num(call))
        
#removing duplicates
bangalore_called_sorted=list(set(bangalore_called_prefix))

        
#lexicographic order
bangalore_called_sorted.sort()
               
print("The numbers called by people in Bangalore have codes:")
for i in bangalore_called_sorted:
    print(i)
    
#Part B:
count=0
for i in bangalore_called_prefix:
    if i=="(080)":
        count+=1

percentage=(count/len(bangalore_called_prefix))*100
percentage=round(percentage,2)

print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")