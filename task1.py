# TASK 1
#   Write a Python program to get the third side of right angled triangle from two given sides.
#   Your program should allow user to input the size of two sides and calculate the other side.
#   Also calculate the area and display the answer in binary format.

#   IMPORT THE MATH MODULE
import math

#   GET SIDE 1
side1 = input("Input the first side: ")
#   CONVERT SIDE 1 TO INTEGER
side1 = int(side1)
#   GET SIDE 2
side2 = input("Input the second side: ")
#   CONVERT SIDE 2 TO INTEGER
side2 = int(side2)
#   DEFINE THE FORMULA
#   SIDE3 = SQUARE ROOT OF (SIDE1)2 + (SIDE2)2
side3 = math.sqrt(pow(side1, 2) + pow(side2, 2))
side3 = int(side3)
#   PRINT SIDE 3
print("Side 3 is: " + str(side3))


#   CALCULATE THE AREA OF THE TRIANGLE
#   TO CALCULATE AREA IS SIDE 1 * SIDE 2 / 2
area = side1 * side2 / 2
area = int(area)

print("The area of the triangle is: " + str(area))
print("The binary area of the triangle is: " + str(bin(area)))
