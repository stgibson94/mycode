#!/usr/bin/env python3

# create variable
message = 'The price of postage is $'

# create input message
mail = float(input("How much does your mail weigh in oz?"))

# create if based on input message
if mail <= 1:
    message = message + '0.55'
elif mail <= 2:
    message = message + '0.75'
elif mail <= 3:
    message = message + '0.95'
elif mail <= 4:
    message = message + '1.15'
elif mail <= 5:
    message = message + '1.35'
else:
    message = 'You will need to send with parcel service.'

# print message to screen
print(message)
