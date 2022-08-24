print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
total_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
# tip = int(input("What percentage tip would you like to give 10, 12, or 15? "))
total_persons = input("How many people to split the bill? ")

bill = float(total_bill)
tip = int(total_tip)
persons = int(total_persons)

bill_with_tip = tip / 100 * bill + bill
# bill_with_tip = bill * (1 + tip / 100)
bill_per_person = bill_with_tip / persons
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

# or
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print("Each person should pay " + final_amount + "$.")
print(f"Each person should pay ${final_amount}.")

