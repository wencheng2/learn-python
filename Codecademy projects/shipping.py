# shipping.py
# Help user find cheapest shipping method for Sal's Shippers task for Codecademy

# Define variables
wgt = float(input("Enter weight of package in lb: "))
print("")

# Ground shipping costs
if wgt <= 2:
  costG = wgt * 1.5 + 20
elif wgt > 2 and wgt <= 6:
  costG = wgt * 3 + 20
elif wgt > 6 and wgt <= 10:
  costG = wgt * 4 + 20
else:
 costG = wgt * 4.75 + 20

format_costG= "{:.2f}".format(costG)
print("Ground Shipping $", format_costG)

# Premium ground shipping costs
costP = 125
format_costP= "{:.2f}".format(costP)

print("")
print("Ground Shipping Premium $", format_costP)

# Drone shipping costs
print("")

if wgt <= 2:
  costD = wgt * 4.5
elif wgt > 2 and wgt <= 6:
  costD = wgt * 9
elif wgt > 6 and wgt <= 10:
  costD = wgt * 12
else:
  costD = wgt * 14.25

format_costD= "{:.2f}".format(costD)
print("Drone Shipping $", format_costD)

# Find cheapest method
list1 = [costG, costP, costD]
list1.sort()

cheap = list1[0]
format_cheap= "{:.2f}".format(cheap)

print("")
if cheap == costG:
  print ("Ground Shipping is the cheapest")
elif cheap == costP:
  print("Ground Shipping Premium is the cheapest")
else:
  print("Drone Shipping is the cheapest")
print("Total cost $", format_cheap)
print("")