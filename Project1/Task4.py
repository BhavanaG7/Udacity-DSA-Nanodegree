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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
#telemarketers->only calling,no receiving texts,no receiving calls,no sending texts
#condition_pass contains only receiving and sending text and receiving call data
def condition_pass(texts,calls):
    dict1=set()
    for i in texts:
        dict1.add(i[0])
        dict1.add(i[1])
        
    for j in calls:
        dict1.add(j[1])
    return dict1
        
def fake_detector(dict1,calls):
    dict2_fake=set()
    for i in calls:
        if i[0] not in dict1:
            dict2_fake.add(i[0])
         
    return dict2_fake

#main
print("These numbers could be telemarketers: ")
l=condition_pass(texts,calls)
fake=fake_detector(l,calls)
new=list(fake)
new.sort()

for i in new:
    print(i)
