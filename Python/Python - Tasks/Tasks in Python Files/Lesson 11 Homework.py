##Task - YPX

print("\n************************************************************************************************************************")

print("                             ***        ***         ** *****              **       **                  ")                                               
print("                              **        **          **     ****            **     **                   ")
print("                               **      **           **        **            **   **                    ")
print("                                **    **            **        **             ** **                     ")
print("                                 **  **             **     ****               ***                      ")                                                                 
print("                                   **               ** *****                  ***                      ")
print("                                   **               **                       ** **                     ")
print("                                   **               **                      **   **                    ")
print("                                   **               **                     **     **                   ")
print("                                   **               **                    **       **                  ")
print("\n************************************************************************************************************************")

enter=input("                                            Press ENTER to continue . . .")

print("\n************************************************************************************************************************")


print("                            MMMMMMMMMMWMMMMMWWNNXXK0OkxxxxxxxkkO0KXXNWWWWWWWMMMMMMMMWWMM")
print("                            MMMMMMMMMMMMMWWNXKOxxdlccc:cdxol:ccclodxk0KXNWWWMMMMMMMMMMMM")
print("                            MMMMMMMMMMMWNX0kdolcol:;;;;oKXKx:;::::oocloxOKXWWWMMMMMMMMMM")
print("                            MMMMMMMMWWNXOdoccc:;;,,,,,cONWWXo,,,,,;;:::ccok0XNWMMMMMMMMM")
print("                            MMMMMMMWNK0xodol:;,,,,,;;cONWWMWKo;,,,'',,:codook0NWWWWMMMMM")
print("                            MMMMMMWN0koccd0K0kolc::clONWWWWMWKdc:c:coxOKKkl:cdOKWWWWMMMM")
print("                            MMWMMWX0dc::;;dXWWWNXKOxONWWWMMWWW0xk0KNNWWNOc;:::lkKNWWMMMM")
print("                            MMMMWN0dlc:;,,:kNWWMMWWWWWWMNNWWMMWWWWWMWWW0c,,,::clkKNWMMMM")
print("                            MMMWN0xlol;,,,;lONWMMMMMMWNXxkXNNWWWMMMMWWKd:,,,,:oookKWWMMM")
print("                            WWWWXkl::;,,,,:coKNWMMMMMWklccodx0WWMMMWWXxc:;,,,;::cd0XWMMM")
print("                            MMWN0dc::;,,;cdkOXWWMMMWW0c;c,'cockNWMWWWN0kxo:,,,;::lkKWWMM")
print("                            MMWXOo:cclok0XNWWMMMMMMNOd:,:;,,cl:xNWWMWWWWWNKOxolcccxKNWWM")
print("                            MMWXOolxOKNWWMWWMMMMMMWkcl:,:::,;lc:0WWWWWMMMMMWWXKkdlx0NWWW")
print("                            WMWXOoccllox0XNWWMMMMMWx;lc':odc,c::0WWWWMMWWNKOxollccxKNMMM")
print("                            WMWX0dc::,,,;ldk0XWWMMW0llo;ckOl,:cxNWMMWNKkxo:;,,;c:lkKNMMM")
print("                            WWKkOkl::;,,,;:cdKWWMMWWKd:,:oo:;lONWMMMWNklc:,,,,:::oOXXXWW")
print("                            WNd;lOdloc;,,,;l0WWWMWWMWXkoodddONWWWWWMWWXx:,,,,;lllx00doKM")
print("                            WXo;:dkdlc:;,,:kNWMMMWWWNWWWWWWWWWWNWWWWWWWKl,,,;:lox0xl;;0M")
print("                            Nk;',;okoc::;;dXWWWNX0kxkXWMMWWWWW0xxOKXNWWNOc;:c:cxko:lccKM")
print("                            WXd,;;.ckdc:cd0KOxolccc:lkNMMMWWWKdcccccodO0Kkl:clkkdc:c;oNM")
print("                            WWWOc'..:xkoldol;,,,,,,;;lOWMMMWXd:;;,,,,,;codllxkoc:,;::OWW")
print("                            MWWWXd;,,:oxxdc:::;;,,,,,,c0WWWXd;,,,,,;;:::cldkdc;'.,clkNMM")
print("                            MMWWXo,,,',;cdkdoc:clc:;;;;dKNXk:;;;;:ll:ccoxxdccdo;,;:kNMMM")
print("                            MMWWN0d:;'.,,,codxxddoc::::cxOxo::cccldddxddol::ll;;;:xNMMMW")
print("                            MMMMMMXl;'.,;,;,';loxddxxdddxxxddddxdddddo:;cll:;;:lo0WMMMMM")
print("                            MMMMMMMKOo,,,'',..',,,:::lol:lxdolllllcloclccc;,;clkNWMMMMMM")
print("                            MMMMMMMMNOc,,,;,,'..,,'..,;'.';:oddlcdlldl:;,;::lxKWWWMMMMMM")
print("                            MMMMMMMMWOdo:'',;,'.,;...',;,,;:l;;olodl;',;,,dKNWWMMMMMMMMM")
print("                            MMMMMMMMWWWWx;;c:;,,'..'...''',....',,,,,,',:dKWMMMMMMMMMMMM")

print("\n************************************************************************************************************************")

print("                                              Welcome to the program!")          
print("             If you want to see informations about the car by entering its licence plate number, press the button 1.")                       
print("                        If you want to see all cars and theirs informations, press the button 2.")  
print("                               If you want to add new penalty to the car, press the button 3.")

number=int(input("\n                                              Enter the number here : "))

while True:
    if(number>3 or number<1):
          number=int(input("                                       Enter 1 or 2 or 3, not other numbers :"))
    else:
        break

if (number==1):
    cars={

                "7E37U3":{
                    "name":"George",
                    "surname":"Marshall",
                    "age":43,
                    "state":"Tennessee (TN)",
                    "make":"Chevrolet",
                    "model":"Impala Lt",
                    "vin":"2G1WT58K079318939",
                    "description":"Chevrolet Impala Lt",
                    "assembly":"No Info",
                    "engine size":"No Info",
                    "registration year":2007,
                    "penalties":["- Driving vehicles dangerously.","- Stop Line Violation"]
                    },
                "6TYZ99S":{
                    "name":"Robyn",
                    "surname":"Matthews",
                    "age":56,
                    "state":"Nevada (NV)",
                    "make":"Mercedes-Benz",
                    "model":"C 230K Sport Sedan",
                    "vin":"WDBRF40J85F650140",
                    "description":"Mercedes-Benz C 230K Sport Sedan",
                    "assembly":"No Info",
                    "engine size":"No Info",
                    "registration year":2005,
                    "penalties":["- Centre Line Violation."]
                },
                "5ZIH427":{
                    "name":"Carolyn",
                    "surname":"Shields",
                    "age":53,
                    "state":"California (CA)",
                    "make":"Toyota",
                    "model":"Highlander",
                    "vin":"JTEGD21A640092495",
                    "description":"Toyota Highlander",
                    "assembly":"No Info",
                    "engine size":"No Info",
                    "registration year":2004,
                    "penalties":["There is no penalties of the citizen."]
                },
                "34GBW21":{
                    "name":"Sebastian",
                    "surname":"Hewitt",
                    "age":32,
                    "state":"California (CA)",
                    "make":"Dodge",
                    "model":"Caravan Se / Sport",
                    "vin":"2B4GP45R7WR707813",
                    "description":"1998 Dodge Caravan Se / Sport",
                    "assembly":"Canada",
                    "engine size":"3.3L V6 MPI",
                    "registration year":1998    ,
                    "penalties":["- Driving vehicle at excessive speed.","- The vehicle without proper Driving Licence.","- Stop Line Violation"]
                },
                "WAHG28":{
                    "name":"Leslie",
                    "surname":"Wise",
                    "age":38,
                    "state":"New Mexico (NM)",
                    "make":"Toyota",
                    "model":"Camry Le/Xle/Se",
                    "vin":"JT2BF12K9T0180264",
                    "description":"Toyota Camry Le/Xle/Se",
                    "assembly":"No Info",
                    "engine size":"No Info",
                    "registration year":1996,
                    "penalties":["- Driving vehicles in violation of Mandatory Traffic Signs.","- Driving vehicle by a drunken person or by a person under influence of drugs."]
                    },
                "BKL8053":{
                    "name":"Julian",
                    "surname":"Weasley",
                    "age":26,
                    "state":"North Carolina (NC)",
                    "make":"Lexus",
                    "model":"Lx 470",
                    "vin":"JT6HT00W6X0024951",
                    "description":"1999 Lexus Lx 470",
                    "assembly":"Japan",
                    "engine size":"4.7L V8 EFI",
                    "registration year":1999,
                    "penalties":["- Stop Line Violation.","- Refusing to go on hire.","- Driving vehicle at excessive speed.","- Driving vehicles in violation of restriction (No Entry Violation)."],
                    },
            }


    
    
    def showCarInfoByLicencePlateNumber(licence_plate_number):
        info=cars[licence_plate_number] 
        print("")
        print("Information about the car is displayed . . .")
        print("")
        print("Name of the owner : ",info["name"])
        print("Surname of the owner : ",info["surname"])
        print("Age of the owner: ",info["age"])
        print("State of the owner :",info["state"])
        print("Make of the car :",info["make"])
        print("Model of the car :",info["model"])
        print("VIN (Vehicle identification number) of the car :",info["vin"])
        print("Description of the car :",info["description"])
        print("Assembly of the car :",info["assembly"])
        print("Engine size of the car :",info["engine size"])
        print("Registration year of the car :",info["registration year"])
        print("")
        print("Penalties of the car :")
        for p in penalties:
            print(p)



    licence_plate_number=input("\nEnter licence plate number : ")
    info=cars[licence_plate_number]
    penalties=info["penalties"]
    showCarInfoByLicencePlateNumber(licence_plate_number)




#######################################################################################################################################################################################################################




elif(number==2):
    car1={
        "seria no":"7E37U3",
        "name":"George",
        "surname":"Marshall",
        "age":43,
        "state":"Tennessee (TN)",
        "make":"Chevrolet",
        "model":"Impala Lt",
        "vin":"2G1WT58K079318939",
        "description":"Chevrolet Impala Lt",
        "assembly":"No Info",
        "engine size":"No Info",
        "registration year":2007,
        "penalties":["1) Driving vehicles dangerously.","2) Stop Line Violation"]
        }

    car2={
        "seria no":"6TYZ99S",
        "name":"Robyn",
        "surname":"Matthews",
        "age":56,
        "state":"Nevada (NV)",
        "make":"Mercedes-Benz",
        "model":"C 230K Sport Sedan",
        "vin":"WDBRF40J85F650140",
        "description":"Mercedes-Benz C 230K Sport Sedan",
        "assembly":"No Info",
        "engine size":"No Info",
        "registration year":2005,
        "penalties":["1) Centre Line Violation."]
        }

    car3={
        "seria no":"5ZIH427",
        "name":"Carolyn",
        "surname":"Shields",
        "age":53,
        "state":"California (CA)",
        "make":"Toyota",
        "model":"Highlander",
        "vin":"JTEGD21A640092495",
        "description":"Toyota Highlander",
        "assembly":"No Info",
        "engine size":"No Info",
        "registration year":2004,
        "penalties":["There is no penalties of the citizen."]
        }

    car4={
        "seria no":"34GBW21",
        "name":"Sebastian",
        "surname":"Hewitt",
        "age":32,
        "state":"California (CA)",
        "make":"Dodge",
        "model":"Caravan Se / Sport",
        "vin":"2B4GP45R7WR707813",
        "description":"1998 Dodge Caravan Se / Sport",
        "assembly":"Canada",
        "engine size":"3.3L V6 MPI",
        "registration year":1998    ,
        "penalties":["1) Driving vehicle at excessive speed.","2) The vehicle without proper Driving Licence.","3) Stop Line Violation"]
        }

    car5={   
        "seria no":"WAHG28",
        "name":"Leslie",
        "surname":"Wise",
        "age":38,
        "state":"New Mexico (NM)",
        "make":"Toyota",
        "model":"Camry Le/Xle/Se",
        "vin":"JT2BF12K9T0180264",
        "description":"Toyota Camry Le/Xle/Se",
        "assembly":"No Info",
        "engine size":"No Info",
        "registration year":1996,
        "penalties":["1) Driving vehicles in violation of Mandatory Traffic Signs.","2) Driving vehicle by a drunken person or by a person under influence of drugs."]
        }

    car6={
        "seria no":"BKL8053",
        "name":"Julian",
        "surname":"Weasley",
        "age":26,
        "state":"North Carolina (NC)",
        "make":"Lexus",
        "model":"Lx 470",
        "vin":"JT6HT00W6X0024951",
        "description":"1999 Lexus Lx 470",
        "assembly":"Japan",
        "engine size":"4.7L V8 EFI",
        "registration year":1999,
                "penalties":["1) Stop Line Violation.","2) Refusing to go on hire.","3) Driving vehicle at excessive speed.","4) Driving vehicles in violation of restriction (No Entry Violation)"]
            }  

    cars=[car1,car2,car3,car4,car5,car6]    


    x=1
    for c in cars:
        print("\n")
        print("About the car",x,":")
        print("")
        print("Licence plate number of the car : ",c["seria no"])
        print("Name of the owner : ",c["name"])
        print("Surname of the owner : ",c["surname"])
        print("Age of the owner: ",c["age"])
        print("State of the owner :",c["state"])
        print("Make of the car :",c["make"])
        print("Model of the car :",c["model"])
        print("VIN (Vehicle identification number) of the car :",c["vin"])
        print("Description of the car :",c["description"])
        print("Assembly of the car :",c["assembly"])
        print("Engine size of the car :",c["engine size"])
        print("Registration year of the car :",c["registration year"])
        x+=1
        print("Penalties of the car :")
        penalties=c["penalties"]
        for p in penalties:
            print(p)


     
####################################################################################################################################################################################################################################




if(number==3):
    cars={
                "7E37U3":{
                    "name":"George",
                    "surname":"Marshall",
                    "age":43,
                    "state":"Tennessee (TN)",
                    "make":"Chevrolet",
                    "model":"Impala Lt",
                    "vin":"2G1WT58K079318939",
                    "description":"Chevrolet Impala Lt",
                    "assembly":"No Info",
                    "engine size":"No Info",
                    "registration year":2007,
                    "penalties":["- Driving vehicles dangerously.","- Stop Line Violation"]
                    },
                "6TYZ99S":{
                    "name":"Robyn",
                    "surname":"Matthews",
                    "age":56,
                    "state":"Nevada (NV)",
                    "make":"Mercedes-Benz",
                    "model":"C 230K Sport Sedan",
                    "vin":"WDBRF40J85F650140",
                    "description":"Mercedes-Benz C 230K Sport Sedan",
                    "assembly":"No Info",
                    "engine size":"No Info",
                    "registration year":2005,
                    "penalties":["- Centre Line Violation."]
                },
                "5ZIH427":{
                    "name":"Carolyn",
                    "surname":"Shields",
                    "age":53,
                    "state":"California (CA)",
                    "make":"Toyota",
                    "model":"Highlander",
                    "vin":"JTEGD21A640092495",
                    "description":"Toyota Highlander",
                    "assembly":"No Info",
                    "engine size":"No Info",
                    "registration year":2004,
                    "penalties":["There is no penalties of the citizen."]
                },
                "34GBW21":{
                    "name":"Sebastian",
                    "surname":"Hewitt",
                    "age":32,
                    "state":"California (CA)",
                    "make":"Dodge",
                    "model":"Caravan Se / Sport",
                    "vin":"2B4GP45R7WR707813",
                    "description":"1998 Dodge Caravan Se / Sport",
                    "assembly":"Canada",
                    "engine size":"3.3L V6 MPI",
                    "registration year":1998    ,
                    "penalties":["- Driving vehicle at excessive speed.","- The vehicle without proper Driving Licence.","- Stop Line Violation"]
                },
                "WAHG28":{
                    "name":"Leslie",
                    "surname":"Wise",
                    "age":38,
                    "state":"New Mexico (NM)",
                    "make":"Toyota",
                    "model":"Camry Le/Xle/Se",
                    "vin":"JT2BF12K9T0180264",
                    "description":"Toyota Camry Le/Xle/Se",
                    "assembly":"No Info",
                    "engine size":"No Info",
                    "registration year":1996,
                    "penalties":["- Driving vehicles in violation of Mandatory Traffic Signs.","- Driving vehicle by a drunken person or by a person under influence of drugs."]
                    },
                "BKL8053":{
                    "name":"Julian",
                    "surname":"Weasley",
                    "age":26,
                    "state":"North Carolina (NC)",
                    "make":"Lexus",
                    "model":"Lx 470",
                    "vin":"JT6HT00W6X0024951",
                    "description":"1999 Lexus Lx 470",
                    "assembly":"Japan",
                    "engine size":"4.7L V8 EFI",
                    "registration year":1999,
                    "penalties":["- Stop Line Violation.","- Refusing to go on hire.","- Driving vehicle at excessive speed.","- Driving vehicles in violation of restriction (No Entry Violation)."],
                    },
            }

    
    
    def showCarInfoByLicencePlateNumber(licence_plate_number):
        info=cars[licence_plate_number] 
        penalties=info["penalties"]
        print("")
        print("Information about the car is displayed . . .")
        print("")
        print("Name of the owner : ",info["name"])
        print("Surname of the owner : ",info["surname"])
        print("Age of the owner: ",info["age"])
        print("State of the owner :",info["state"])
        print("Make of the car :",info["make"])
        print("Model of the car :",info["model"])
        print("VIN (Vehicle identification number) of the car :",info["vin"])
        print("Description of the car :",info["description"])
        print("Assembly of the car :",info["assembly"])
        print("Engine size of the car :",info["engine size"])
        print("Registration year of the car :",info["registration year"])
        print("")
        print("Penalties of the car :")
        for p in penalties:
            print(p)
      
            
    licence_plate_number=input("\nEnter the licence plate number of the car : ")
    showCarInfoByLicencePlateNumber(licence_plate_number)
    info=cars[licence_plate_number]
    penalties=info["penalties"]

    def printPenalties():
        for x in penalties:
            print(x)

    def addPenalty():
        newPenalty=input("\nEnter the new penalty : ")
        if(licence_plate_number=="5ZIH427"):
            info.pop("penalties")
            print("\nPenalties of the car :")
            print("-",newPenalty)
        else:
            print("\nPenalties of the car :")
            printPenalties()
            print("-",newPenalty)

    addPenalty()



#############################################################################################################################################################################################################
