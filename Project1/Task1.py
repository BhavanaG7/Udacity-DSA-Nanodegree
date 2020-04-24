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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
total_data=texts+calls
dict1=set()
for individual_list in total_data:
    t1=individual_list[0]
    t2=individual_list[1]

    dict1.add(t1)
    dict1.add(t2)

count=len(dict1)

print(f"There are {count} different telephone numbers in the records.")