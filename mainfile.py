#the .py module are importing
import rentfile
import returnfile
import Displayfile

#Welcomes function is calling from Displayfile
Displayfile.Welcomes()
continueLoop = True
#repitition for while loop
while continueLoop == True:
    #pick function is called from Displayfile
    Displayfile.pick()
    continueCorrectOption = False
    while continueCorrectOption == False:
        #try and catch is used For catching expectation 
        try:
            option = int(input("Enter an option: "))
            continueCorrectOption = True
        except:
            #Inapplicable_options is called from Displayfile
            Displayfile.Inapplicable_options()
            Displayfile.pick()
   #condition is given according to option
            
    if option == 1:
        rentfile.rent_costume ()   
    elif option == 2:
        returnfile.return_costume()
    elif option == 3:
        Displayfile.Exit ()
        continueLoop = False 
    else:
        Displayfile.inapplicable()
