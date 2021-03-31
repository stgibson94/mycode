#!/usr/bin/env python3

import csv

# make a file for users inputs
f = open("csv_users.txt", "r")

# create counter to loop through each line of file
i = 0


# turn each row of file into a comma seperated value
for row in csv.reader(f):
    i = i + 1 # incrementer (could also be i += 1

    # creating a file name for csv data
    filename = "admin.rc%d"%(i)

    # open the file
    rcfile = open(filename, "w")

    # write in the values row by row
    print("export OS_AUTH_URL=" + row[0], file=rcfile)
    print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
    print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
    print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
    print("export OS_USERNAME=" + row[3], file=rcfile)
    print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
    print("export OS_PASSWORD=" + row[5], file=rcfile)
    
    # close file
    rcfile.close()
