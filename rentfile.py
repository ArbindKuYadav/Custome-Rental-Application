#importing datetime,random,Displayfile and rentmission
import datetime
import random
import Displayfile
import rentmission
#for generating bill defining by this function
def rent_costume():
    #Rent is calling from displayfile
    Displayfile.rent()
    rentmission.ballot()
    rentmission.rent_dictionary()
    dictionaryCostume = rentmission.rent_dictionary()
    rentCostumeID = rentmission.proper_costume_ID()
    rented_costumes = []
    items_brand = []
    #the quantity condition updating
    if int(dictionaryCostume[rentCostumeID][3]) > 0:
        Displayfile.material_available()
        amt = rentmission.portion(int(dictionaryCostume[rentCostumeID][3]))
        dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3])- amt
        print(dictionaryCostume)
        
        customer_name = input("\nEnter the name of customer: ")
        
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        price = rentmission.overall_price(dictionaryCostume,amt,rentCostumeID)
        
        rented_costumes.append(dictionaryCostume[rentCostumeID][0])
        rentmission.stock_material(dictionaryCostume)
        
        items_brand.append(dictionaryCostume[rentCostumeID][1])
        rentmission.stock_material(dictionaryCostume)
        
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Does the customer want to rent another costume as well??")
        rentMORE = input("Please enter 'Y' if the customer wants to rent another costume else provide any other value: ").upper()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")        
        loop = True
        while loop == True:
            if rentMORE == "Y":
                Displayfile.rent()
                rentmission.ballot()
                dictionaryCostume = rentmission.rent_dictionary()
                rentCostumeID = rentmission.proper_costume_ID()
                
                if int(dictionaryCostume[rentCostumeID][3]) > 0:
                    Displayfile.material_available()
                    
                    amt = rentmission.portion(int(dictionaryCostume[rentCostumeID][3]))
                    dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) - amt
                    print(dictionaryCostume)
                    
                    rented_costumes.append(dictionaryCostume[rentCostumeID][0])
                    rentmission.stock_material(dictionaryCostume)
                    
                    items_brand.append(dictionaryCostume[rentCostumeID][1])
                    rentmission.stock_material(dictionaryCostume)
                    
                    price = rentmission.overall_price(dictionaryCostume,amt,rentCostumeID) + price
                    
                    print()
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("Does the customer want to rent another costume as well??")
                    rentMORE = input("Please enter 'Y' if the customer wants to rent another costume else provide any other value: ").upper()
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  

            else:
                print()
                print("====================================================")
                print("                    Bill Details                    ")
                print("====================================================")
                print("****************************************************")
                print("Name of Customer: ", customer_name)
                print()
                print("Date and time of rent: ", date_time)
                print()
                print("Total Price: $", price)
                print()
                print("Items Rented are: ",", ".join(rented_costumes))
                print()
                print("Brand of the Items are: ",", ".join(items_brand))
                print("****************************************************")
                print()
                print("+++++++++++++++++++++++++++++++++++++++++++++++++")
                print("|     Rent Details Bill has been generated.     |")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++")
                print()
                
                num=str(random.randint(999999999,9999999999))
                bill = open("Rent_"+customer_name+"_"+num+".txt","w")
                bill.write("===============================================\n")
                bill.write("                   Invoice                    \n")
                bill.write("===============================================\n")
                bill.write(" Name of Customer: " + str(customer_name))
                bill.write("\n Date and time of rent: " +str(date_time))
                bill.write("\n Total Price: $" + str(price))
                bill.write("\n Items rented are: " + ", ".join(rented_costumes))
                bill.write("\n Brand of the Items are: " +", ".join(items_brand))
                bill.write("\n===============================================")
                bill.close()
                loop = False
    else:
        Displayfile.material_unavailable()    
