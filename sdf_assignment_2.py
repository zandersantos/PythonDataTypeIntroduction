"""
Description: Introduction to Python: Declaring and Using Variables
Author: Zander Santos
Date: September. 21, 2023
Usage: To gain experience with the different data types on python
"""

#SIMPLE DATA TYPES
name = "Zander"
print("value:" , " " , name , " " , "type:" , " " ,  type(name))

validManitobaDriversLicence = True
print("value:" , " " , validManitobaDriversLicence , " " , "type:" , " " ,  type(validManitobaDriversLicence))

currentYear =  2023
print("this year:" , " " , currentYear , " " , "type:" , " " ,  type(currentYear))

currentYear += 1
print("next year:" , " " , currentYear , " " , "type:" , " " ,  type(currentYear))

#CALCULATIONS
GST = 5.00
PST = 7.00

vehicleCost = 61000.5

print("pre-tax value:" , vehicleCost , " PST: ", PST, " GST: ", GST, "total: ", vehicleCost + ((GST * vehicleCost)/100) + ((PST * vehicleCost)/100) )
print(f"pre-tax value: ${vehicleCost:,.2f}", f" PST: {PST:,.2f}", f" GST: {GST:,.2f}", f" total: ${vehicleCost + ((GST * vehicleCost)/100) + ((PST * vehicleCost)/100):,.2f}")


#LISTS

#TUPLES

#DICTIONARIES

#SETS

