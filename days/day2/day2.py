print("Welcome to the tip calculator!")

total_bil = float(input("What was the total bill?"))

the_tip = float(input("How much tip would you like to give? 10, 12, or 15?"))
account_of_people = int(input("How many people to split the bill?"))
total_bil_for_each_person = ((total_bil / account_of_people) * (1 + (the_tip / 100)))
print(f'Each person should pay: ${total_bil_for_each_person:.2f} ')
