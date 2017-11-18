print("We are going to figure out which two numbers divide evenly with one another.")
num = float(raw_input("Give me 2 numbers. 1st number: "))
check = float(raw_input("2nd number: "))
if num % check == 0:
    print( "%d divides evenly by %d") % (num, check)
else:
    print("%d does not divide evenly by %d. Sorry.") % (num, check)
