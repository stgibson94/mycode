#!/usr/bin/env python3

# open file
outFile = open("admin.rc", "a")

# prompt user for OS auth url and print to file
osAUTH = input("What is the OS_AUTH_URL?")
print("export OS_AUTH_URL=" + osAUTH, file=outFile)

# print os identity line to file
print("export OS_IDENTITY_API_VERSION=3", file=outFile)

# prompt user for project name and print to file
osPROJ = input("What is the OS_PROJECT_NAME?")
print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

# prompt user for domain name and print to file
osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME?")
print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

# promt user for username and print to file
osUSER = input("What is the OS_USERNAME?")
print("export OS_USERNAME=" + osUSER, file=outFile)

# promt user domain name and print to file
osUSERDOM = input("What is the OS_USER_DOMAIN_NAME?")
print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

# prompt user for pass and print to file
osPASS = input("What is the OS_PASSWORD?")
print("export OS_PASSWORD=" + osPASS, file=outFile)

# close the file
outFile.close()
