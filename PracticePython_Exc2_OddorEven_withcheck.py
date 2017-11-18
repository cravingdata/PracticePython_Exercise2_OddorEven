print("We are going to figure out which two numbers divide evenly with one another.")
num = float(raw_input("Give me 2 numbers. 1st number: "))
check = float(raw_input("2nd number: "))
if num % check == 0:
    print("The 1st number divides evenly with the 2nd number.")
else:
    print("These two numbers do not divide evenly. Sorry.")
