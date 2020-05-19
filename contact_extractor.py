"""
This script extracts every phone number and email address in a long
wep page or document.

"""

import re 

# creating a regex for phone numbers

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code (group 1)
    (\s|-|\.)               # separator
    (\d{3})                   # first 3 digits (group 3)
    (\s|-|\.)               # separator
    (\d{4})                   # last 4 digits (group 5)
    )''', re.VERBOSE)


# creating email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # string after the dot.
    )''', re.VERBOSE)


# finding matches in text

def findPhoneNumberMatches(text):
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNumber = '-'.join([groups[1], groups[3], groups[5]])
        matches.append(phoneNumber)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])
    return matches

def saveToTxt(result):
    textFile = open("results.txt", "w")
    for i, line in enumerate(result):
        textFile.write(f'{i+1}) {line}\n')
    textFile.close()


if __name__ == "__main__":
    result = findPhoneNumberMatches("text goes here")
    saveToTxt(result)