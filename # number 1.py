# number 1
import math

m = float(input("Enter the mass of the cart (in kg): "))
f = float((input("Enter the force to push the cart (in N): ")))
g = 9.8

degree = f/(m*g)

radian = math.asin(degree)
converting= math.degrees(radian)
print ("The angle of the ramp is", "{:,.1f}".format(converting), "degrees")

# input the mass
# input the force
# process begin on degree by calculating
# the calculation will be show on the last line