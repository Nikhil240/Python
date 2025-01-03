print("Welcome to the tip calculator!!")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
tippercent = (tip/100) * bill
total = bill+tippercent
split = int(input("How many people to split the bill?\n"))
Finalbill = total/split
print("Each person should pay:",Finalbill)
