#SHIPPING PROCESS..........
weight = 80
#Ground shipping....
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight == 6:
  cost_ground = weight * 3.00 + 20
elif weight == 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print(cost_ground)

cost_ground_premium = 125.00

#Ground shipping premium........
print("Ground Shipping Premium $", cost_ground_premium)

#Drone shipping...........

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 2:
  cost_drone = weight * 9.00
elif weight <= 2:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.00

print("Drone Shipping: $", cost_drone)

#end..............