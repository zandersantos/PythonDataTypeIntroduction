"""
Description: Introduction to Python: Declaring and Using Variables
Author: Zander Santos
Date: September. 21, 2023
Usage: To gain experience with the different data types on python
"""

#SIMPLE DATA TYPES

    # string data type
name = "Zander"
print("value:", name , "type:", type(name))

    # boolean data type
validManitobaDriversLicence = True
print("value:", validManitobaDriversLicence, "type:", type(validManitobaDriversLicence))

    # int data type
currentYear =  2023
print("this year:", currentYear, "type:", type(currentYear))

currentYear += 1
print("next year:", currentYear, "type:", type(currentYear))

#CALCULATIONS
GST = 5.00
PST = 7.00

vehicleCost = 61000.5

    # prints pre-tax value, gst, pst and also calculates the vehicle cost + gst of vehicle + pst of vehicle
print("pre-tax value:",
      vehicleCost,
      "PST:",
      PST,
      "GST:",
      GST,
      "total:",
      vehicleCost + ((GST * vehicleCost)/100) + ((PST * vehicleCost)/100))

    # ,.2f gives it a decimal placement of 2 while also adding a , so it look like a value amount
print(f"pre-tax value: ${vehicleCost:,.2f}",
      f" PST: {PST:,.2f}",
      f" GST: {GST:,.2f}",
      f" total: ${vehicleCost + ((GST * vehicleCost)/100) + ((PST * vehicleCost)/100):,.2f}")

#LISTS

    # list 1 through 10
listOneToTen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(listOneToTen))
print(listOneToTen)

    # inserts Zander in the 5th position of the list which is inbetween 5 and 6
listOneToTen.insert(5,"Zander")
print(listOneToTen)

    # removes 9 value
listOneToTen.remove(9)
print(listOneToTen)

    # list containing A B C
listABC = ["A","B","C"]

    # a combination of listOneToTen and listABC
listCombination = listOneToTen + listABC
print(listCombination)


#TUPLES
provinces = ('Manitoba', 'Alberta', 'Ontario', 'Nova Scotia')
print(provinces)
print(type(provinces))

#DICTIONARIES
dictionaryCoins = {'nickel': 0.05, 'dime': 0.1, 'quarter': 0.25}
print(dictionaryCoins)

print(type(dictionaryCoins))

    # change decimal point
dictionaryCoins = {'nickel': 5, 'dime': 1, 'quarter': 25}
print(dictionaryCoins)

    # inserts 2 new items to dict
dictionaryCoins['loonie'] = 100
dictionaryCoins['toonie'] = 200
print(dictionaryCoins)

#SETS


setMultiplesOf2 = {2,4,6,8,10,12,14,16,18,20}
print(setMultiplesOf2)
print(type(setMultiplesOf2))

setMultiplesOf5 = {5,10,15,20}
print(setMultiplesOf5)

    # creates a set of all unique numbers in sets setMultipleOf2 and setMultipleOf5 (no repeats)
setUnique = setMultiplesOf2.union(setMultiplesOf5)
print(setUnique)

    # creates a set of values that appear in both sets
setCombination = setMultiplesOf2.intersection(setMultiplesOf5)
print(setCombination)

    # creates a set that only appears in setMultipleOf2
setOnlyIn2 = setMultiplesOf2.difference(setMultiplesOf5)
print(setOnlyIn2)

    # creates a set that only appears in setMultipleOf5
setOnlyIn5 = setMultiplesOf5.difference(setMultiplesOf2)
print(setOnlyIn5)
