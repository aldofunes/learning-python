import sys


password = input("Please enter a super secret password:  ")
attempt_count = 1
while True:
    print("Attempt number {}".format(attempt_count))
    attempt_count += 1
     
attempt_count = 1
while password != "opensesame":
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid pasword, try again:  ")
    attempt_count += 1

print("Welcome to secret town")