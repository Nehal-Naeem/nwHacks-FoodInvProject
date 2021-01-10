# Dictionaries
itemName = {}
itemExpiry = {}
itemStock = {}


# read method
# reads from iventory.txt to variable data

def getData():
    data = open("inventory.txt", "r+")
    return data

# toDictionary method
# import Inventory from file object to dictionaries relevant to our Inventory system
# each item is identified by unique ID/ part number and 3 dictionaries
# not sure about stock option I dont know if its relevant but included it anyway
# didnt include product type because thought it was irrelevant

# expiry date is written as mm/dd/yyyy format in text file, and as [mm, dd, yyyy] in dictionary itemExpiry
# 
def toDictionaries(fileObject) :
    itemCount = int((fileObject.readline()).rstrip('\n'))
    for i in range(0, itemCount):
        line = (fileObject.readline()).rstrip("\n")
        
        x0, x1, x2, x3 = line.split("#")
        month, day, year = x2.split("/")
    
        x0 = int(x0)
        x3 = int(x3)
        month = int(month)
        day = int(day)
        year = int(year)

        itemName.update({x0: x1})
        itemExpiry.update({x0: [month, day, year]})
        itemStock.update({x0: x3})

    # print(x1)

    # print("Expiry Month is:" ,month)
    # print(day)
    # print(year)
    
    # print(x3)


# mess around with inventory.txt to see different results

test= getData()
toDictionaries(test)
print(itemName, itemExpiry, itemStock)
