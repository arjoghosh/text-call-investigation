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

# For each incoming and answering number in texts and calls database,
# we add the numbers into a set, so that the unique phone number will be saved.
phone_numbers = set()

for record in texts:
    phone_numbers.add(record[0])
    phone_numbers.add(record[1])

for record in calls:
    phone_numbers.add(record[0])
    phone_numbers.add(record[1])

print("There are {} different telephone numbers in the record".format(len(phone_numbers)))
