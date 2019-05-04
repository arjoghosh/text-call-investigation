"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

CALLING_TIME = {}

def process_calling_time(phone_number, duration):
    if CALLING_TIME.get(phone_number) is None:
        CALLING_TIME[phone_number] = duration
    else:
        CALLING_TIME[phone_number] += duration

for call in calls:
    from_phone_number = call[0]
    to_phone_number = call[1]
    duration = call[3]
    process_calling_time(from_phone_number, duration)
    process_calling_time(to_phone_number, duration)

sorted_call_time = sorted(CALLING_TIME.items(), key= lambda d: d[1], reverse=True)
result_number = sorted_call_time[0][0]
result_duration = sorted_call_time[0][1]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(result_number, result_duration))
