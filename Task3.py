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

PREFIX_FIXED_LINE = '('
SURFIX_FIXED_LINE = ')'
PREFIX_MOBILE = ['7', '8', '9']
BANGALORE = '080'

# Predefined methods
def is_in_bangalore(phone_number):
  if phone_number[0] == PREFIX_FIXED_LINE:
    code_area = phone_number[1:4]
  else:
    code_area = phone_number

  if code_area == BANGALORE:
    return True
  return False

def process_answering_number(phone_number):
  if phone_number[0] == PREFIX_FIXED_LINE:
    return phone_number.split(SURFIX_FIXED_LINE, 1)[0][1:]
  else:
    return phone_number[0:4]
  return 0


# Processing script
list_of_codes = set()
total_calls_from_bangalore = 0
total_calls_from_bangalore_to_bangalore = 0

for call in calls:
  if is_in_bangalore(call[0]):
    total_calls_from_bangalore += 1
    result = process_answering_number(call[1])
    list_of_codes.add(result)

    if is_in_bangalore(result):
      total_calls_from_bangalore_to_bangalore += 1

# Part A Result
list_of_codes = sorted(list_of_codes, reverse=False)
print("The numbers called by people in Bangalore have codes:")
for code in list_of_codes:
  print(code)

# Part B Result
ratio = float(total_calls_from_bangalore_to_bangalore) / float(total_calls_from_bangalore)
percentage = "{0:.2%}".format(ratio)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
