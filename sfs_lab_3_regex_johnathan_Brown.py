# SFS Lab 3 - Python Regex Questions
# EC May, 2022
# Add your answer to each of the questions
import re


# Q1 Import the apache log and print out the contents
# your code here
access_log = "apache_log"
with open(access_log, 'r') as f:
    for line in f:
        #print(line.strip())
# once you have answer for Q1 comment out the print statement to keep things tidy
# Q2 Use regex to find any instance of the word notice?
# your code here
with open ("apache_log") as f:
    file = f.read()
    x = re.findall('notice', file)
    print(f"Number of 'notice' occurrences: {len(x)}")
# Q3 Use regex to find any instance of the word error?
# your code here
with open(access_log) as f:
    file = f.read()
    x = re.findall(r'error', file, re.IGNORECASE)
    print(f"Number of 'error' occurrences: {len(x)}")
# Q4 Use regex to count any instance of the word notice?
# your code here
with open(access_log) as f:
    file = f.read()
    notice_count = len(re.findall(r'notice', file, re.IGNORECASE))
    print(f"Notice count: {notice_count}")
# Q5 Use regex to count any instance of the word error?
# your code here
with open(access_log) as f:
    file = f.read()
    error_count = len(re.findall(r'error', file, re.IGNORECASE))
    print(f"Error count: {error_count}")
# Q6 Use regex to count any instance of the letter p?
# your code here
with open(access_log) as f:
    file = f.read()
    p_count = len(re.findall(r'p', file, re.IGNORECASE))
    print(f"Letter 'p' count: {p_count}") 
# Q7 Use regex to find any instance of the string jk2_init?
# your code here
with open(access_log) as f:
    file = f.read()
    jk2_matches = re.findall(r'jk2_init', file)
    print(f"'jk2_init' occurrences: {len(jk2_matches)}")
# Q8 Use regex to find any appearance of the number 6754?
# your code here
with open(access_log) as f:
    file = f.read()
    matches_6754 = re.findall(r'6754', file)
    print(f"Number '6754' occurrences: {len(matches_6754)}")
# Q9 Use regex to find any appearance of the number 6?
# your code here
with open(access_log) as f:
    file = f.read()
    matches_6 = re.findall(r'6', file)
    print(f"Number '6' occurrences: {len(matches_6)}")
# Q10 Use regex to find any ip addresses?
# your code here
with open(access_log) as f:
    file = f.read()
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ip_addresses = re.findall(ip_pattern, file)
    print(f"IP addresses found: {ip_addresses}")
# Q11 Create a script that will ask for user input, ask the user to enter a letter, then use regex to return any matches of that letter in the file?
# your code here
letter = input("Enter a letter to search for: ")
with open(access_log) as f:
    file = f.read()
    letter_matches = re.findall(re.escape(letter), file, re.IGNORECASE)
    print(f"Occurrences of '{letter}': {len(letter_matches)}")
# Q12 adapt your answer from Q11, to use a function to search the file, the function should take one parameter - the letter you are searching for?
# your code here
def search_letter(letter):
    with open(access_log) as f:
        file = f.read()
        matches = re.findall(re.escape(letter), file, re.IGNORECASE)
        return len(matches)

letter = input("Enter a letter to search for using the function: ")
print(f"Occurrences of '{letter}': {search_letter(letter)}")

