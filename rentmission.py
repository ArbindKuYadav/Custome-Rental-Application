#importing Displayfile
import Displayfile

def ballot():
    file = open("costumes.txt","r")
    print("----------------------------------------------------------")
    print("  ID\tCustomer Name\tCostume Brand\tPrice\tQuantity")
    print("----------------------------------------------------------")
    counterID = 0
    for line in file:
        counterID = counterID + 1
        print(" ",counterID, "\t" + line.replace(",","\t"))
    file.close()
    print("----------------------------------------------------------")

def rent_dictionary():
    file = open("costumes.txt", "r")
    counterID = 0
    dictionaryCostume = {}
    for line in file: 
        counterID = counterID + 1
        line = line.replace("\n","")
        line = line.split(',')
        dictionaryCostume[counterID] =  line
    return dictionaryCostume

def proper_costume_ID():
    try:
        costumeID = int(input("Enter the ID of costume you want to rent: "))
        while costumeID <= 0 or costumeID > len(rent_dictionary()):
            Displayfile.proper()
            ballot()
            costumeID = int(input("\nEnter the ID of costume you want to rent: "))
        return costumeID
    except:
        Displayfile.inoperative_input()
        proper_costume_ID()
        
def portion(stock):
    error = False
    while error == False:
        try:
            amt = int(input("Enter the quantity: "))
            while amt <=0 or amt > stock:
                if amt <= 0:
                    Displayfile.proper_quantity()
                else:
                    Displayfile.further_quantity()
                amt = int(input("Enter the quantity: "))
            return amt
            error = True
        except:
            Displayfile.inapplicable()
        
def stock_material(dictionary):
    file = open("costumes.txt","w")
    for i in dictionary.values():
        line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3])) 
        file.write(line)
        file.write("\n")
    file.close()

def overall_price(dictionary, quantityDetails, rentCostumeID):
    price = float(dictionary[rentCostumeID][2].replace("$",""))
    print("\nThe price of costume:", price)
    pricePerItem = price * quantityDetails
    return pricePerItem

