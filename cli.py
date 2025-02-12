# Inputs We Need From The User
# Total Rent
# Total Food Ordered For Snacking
# Electricity Units Spends
# Charge Per Unit
#Persons Living In Room/Flat

# Output
#Total Amount You'Ve To Pay Is

rent = int(input("Enter Your Hostel/Flat Rent = "))
food = int(input("Enter The Amount Of Food Ordered = "))
electricity_spend = int(input("Enter The Total Of Electricity Spend = "))
charge_per_unit = int(input("Enter The Charge Per Unit = "))
persons = int(input("Enter The Number Of Persons Living In Room/Flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each Person Will Pay = ", output)
