print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
perc_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

tip = (float(total_bill) * (1 + float(perc_tip) / 100)) / float(num_people) 

print(f"Each person should pay: ${tip:.2f}")