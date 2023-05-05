import os
clear = lambda: os.system('cls')

def s():
    print()

with open("totalpayment.txt","w") as tp:
    tp.write("Receipt :")

with open("gasolines.txt","w") as gasolines:
    gasolines.write("AI92 - 1.0 dollar, ")
    gasolines.write("AI95 - 1.4 dollar, ")
    gasolines.write("Disel - 0.8 dollar")

with open("foods.txt","w") as foods:
    foods.write("Hamburger - 1.5 dollar, ")
    foods.write("Sandwich - 2 dollar, ")
    foods.write("Cheeseburger - 1.5 dollar, ")
    foods.write("Coca-Cola - 0.7 dollar, ")
    foods.write("Fanta - 0.7 dollar")

with open("admins.txt","w") as ad:
    ad.write("Admin - 12345678")


def welcome():
    print("MAIN MENU")
    print("\nWelcome to the Gas Station.")
    guestOrAdmin = input("Are you Guest (1) or Admin (2) : ")
    while True:
        if (guestOrAdmin == "1"):
            clear()
            choosePurchaseMethod()
            break
        elif (guestOrAdmin == "2"):
            clear()
            adminCheck()
            break
        else:
            guestOrAdmin = input("Please enter 1 (Guest) or 2 (Admin) : ")

def mainMenu():
    welcome()

def choosePurchaseMethod():
    s()
    choiceOfPurchase = int(input("Choose purchase method\nWith liters (1) | With money (2) : "))
    while True:
        if (choiceOfPurchase == 1):
            chooseTypeOfGasolineLiter()
            break
        elif (choiceOfPurchase == 2):
            chooseTypeOfGasolineMoney()
            break
        else:
            choiceOfPurchase = int(input("Please, enter 1 or 2 : "))

def chooseTypeOfGasolineLiter():
    clear()
    with open("gasolines.txt","r") as gasolines:
        for gasolines in gasolines.readlines():
            g = gasolines
        gasolineList = g.split(", ")
        showInfoOfGasolines = [gasolineList[0],gasolineList[1],gasolineList[2]]
        s()
        for x in showInfoOfGasolines:
            print(x)
        
    choiceOfGasoline = int(input("\nWhich gasoline do you want to buy ?\nAI92 (1) | AI95 (2) | Disel (3) : "))

    while True:
        if (choiceOfGasoline == 1 or choiceOfGasoline == 2 or choiceOfGasoline == 3):
            break
        else:
            choiceOfGasoline = int(input("Please, enter 1 (AI92) or 2 (AI95) or 3 (Disel) : "))
    clear()
    litersOfGasoline = float(input("\nHow many liters of gasoline will you get ?\n- "))

    with open("gasolines.txt","r") as gasolines:
        for gasolines in gasolines.readlines():
            g = gasolines
        split = g.split(",")
        AI92value = split[0].split(" - ")[1].split(" ")[0].strip()
        AI95value = split[1].split(" - ")[1].split(" ")[0].strip()
        Diselvalue = split[2].split(" - ")[1].split(" ")[0].strip()
    if (choiceOfGasoline == 1):
        clear()
        priceAI92 = litersOfGasoline * float(AI92value)    
        if (priceAI92 == int(priceAI92)):
            print("\nAmount to pay for gasoline is \b",int(priceAI92),"dollars.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : AI92.")
                tp.write("\n")
                tp.write("Price of gasoline : 1$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(litersOfGasoline))
                tp.write(" liters.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount to pay for gasoline is ")
                tp.write(str(int(priceAI92)))
                tp.write(" dollars.")
            doYouWantFood()
        else:
            print("\nAmount to pay for gasoline is \b",int(priceAI92),"dollars",int(100 * (priceAI92 - int(priceAI92))),"cents.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : AI92.")
                tp.write("\n")
                tp.write("Price of gasoline : 1$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(litersOfGasoline))
                tp.write(" liters.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount to pay for gasoline is ")
                tp.write(str(int(priceAI92)))
                tp.write(" dollar ")
                tp.write(str(int(100 * (priceAI92 - int(priceAI92)))))
                tp.write(" cents.")
            doYouWantFood()
             
    elif (choiceOfGasoline == 2):
        priceAI95 = litersOfGasoline * float(AI95value)
        if (priceAI95 == int(priceAI95)):
            print("\nAmount to pay for gasoline is \b",int(priceAI95),"dollars.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : AI95.")
                tp.write("\n")
                tp.write("Price of gasoline : 1.4$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(litersOfGasoline))
                tp.write(" liters.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount to pay for gasoline is ")
                tp.write(str(int(priceAI95)))
                tp.write(" dollars.")
            doYouWantFood()
        else:
            print("\nAmount to pay for gasoline is \b",int(priceAI95),"dollars",int(100 * (priceAI95 - int(priceAI95))),"cents.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : AI95.")
                tp.write("\n")
                tp.write("Price of gasoline : 1.4$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(litersOfGasoline))
                tp.write(" liters.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount to pay for gasoline is ")
                tp.write(str(int(priceAI95)))
                tp.write(" dollar ")
                tp.write(str(int(100 * (priceAI95 - int(priceAI95)))))
                tp.write(" cents.")
            doYouWantFood()

    elif (choiceOfGasoline == 3):
        priceDisel = litersOfGasoline * float(Diselvalue)
        if (priceDisel == int(priceDisel)):
            print("\nAmount to pay for gasoline is \b",int(priceDisel),"dollars.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : Disel.")
                tp.write("\n")
                tp.write("Price of gasoline : 0.8$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(litersOfGasoline))
                tp.write(" liters.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount to pay for gasoline is ")
                tp.write(str(int(priceDisel)))
                tp.write(" dollars.")
            doYouWantFood()
        else:
            print("\nAmount to pay for gasoline is \b",int(priceDisel),"dollars",int(100 * (priceDisel - int(priceDisel))),"cents.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : Disel.")
                tp.write("\n")
                tp.write("Price of gasoline : 0.8$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(litersOfGasoline))
                tp.write(" liters.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount to pay for gasoline is ")
                tp.write(str(int(priceDisel)))
                tp.write(" dollar ")
                tp.write(str(int(100 * (priceDisel - int(priceDisel)))))
                tp.write(" cents.")        
            doYouWantFood()
       
def chooseTypeOfGasolineMoney():
    clear()
    with open("gasolines.txt","r") as gasolines:
        for gasolines in gasolines.readlines():
            g = gasolines
        gasolineList = g.split(", ")
        showInfoOfGasolines = [gasolineList[0],gasolineList[1],gasolineList[2]]
        s()
        for x in showInfoOfGasolines:
            print(x)

    choiceOfGasoline = int(input("\nWhich gasoline do you want to buy ?\nAI92 (1) | AI95 (2) | Disel (3) : "))

    while True:
        if (choiceOfGasoline == 1 or choiceOfGasoline == 2 or choiceOfGasoline == 3):
            break
        else:
            choiceOfGasoline = int(input("Please, enter 1 (AI92) or 2 (AI95) or 3 (Disel) : "))

    clear()
    dollarsOfGasoline = float(input("\nHow many dollars of gasoline will you get ?\n- "))

    with open("gasolines.txt","r") as gasolines:
        for gasolines in gasolines.readlines():
            g = gasolines
        split = g.split(",")
        AI92value = split[0].split(" - ")[1].split(" ")[0].strip()
        AI95value = split[1].split(" - ")[1].split(" ")[0].strip()
        Diselvalue = split[2].split(" - ")[1].split(" ")[0].strip()

    if (choiceOfGasoline == 1):
        priceAI92 = dollarsOfGasoline / float(AI92value)    
        if (priceAI92 == int(priceAI92)):
            print("\nAmount of gasoline is \b",int(priceAI92),"liters.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : AI92.")
                tp.write("\n")
                tp.write("Price of gasoline : 1$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(dollarsOfGasoline))
                tp.write(" dollars of AI92.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount of gasoline is ")
                tp.write(str(int(priceAI92)))
                tp.write(" liters.")
            doYouWantFood()
        else:
            print("\nAmount of gasoline is \b",int(priceAI92),"liters",int(100 * (priceAI92 - int(priceAI92))),"milliliters.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : AI92.")
                tp.write("\n")
                tp.write("Price of gasoline : 1$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(dollarsOfGasoline))
                tp.write(" dollars of AI92.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount of gasoline is ")
                tp.write(str(int(priceAI92)))
                tp.write(" liters ")
                tp.write(str(int(100 * (priceAI92 - int(priceAI92)))))
                tp.write(" milliliters.")
            doYouWantFood()
             
    elif (choiceOfGasoline == 2):
        priceAI95 = dollarsOfGasoline / float(AI95value)
        if (priceAI95 == int(priceAI95)):
            print("\nAmount of gasoline is is \b",int(priceAI95),"liters.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : AI95.")
                tp.write("\n")
                tp.write("Price of gasoline : 1.4$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(dollarsOfGasoline))
                tp.write(" dollars of AI95.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount of gasoline is ")
                tp.write(str(int(priceAI95)))
                tp.write(" liters.")
            doYouWantFood()
        else:
            print("\nAmount of gasoline is \b",int(priceAI95),"liters",int(100 * (priceAI95 - int(priceAI95))),"milliliters.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : AI95.")
                tp.write("\n")
                tp.write("Price of gasoline : 1.4$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(dollarsOfGasoline))
                tp.write(" dollars of AI95.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount of gasoline is ")
                tp.write(str(int(priceAI95)))
                tp.write(" liters ")
                tp.write(str(int(100 * (priceAI95 - int(priceAI95)))))
                tp.write(" milliliters.")
            doYouWantFood()

    elif (choiceOfGasoline == 3):
        priceDisel = dollarsOfGasoline / float(Diselvalue)
        if (priceDisel == int(priceDisel)):
            print("\nAmount of gasoline is \b",int(priceDisel),"liters.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : Disel.")
                tp.write("\n")
                tp.write("Price of gasoline : 0.8$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(dollarsOfGasoline))
                tp.write(" dollars of Disel.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount of gasoline is ")
                tp.write(str(int(priceDisel)))
                tp.write(" liters.")
            doYouWantFood()
        else:
            print("\nAmount of gasoline is \b",int(priceDisel),"liters",int(100 * (priceDisel - int(priceDisel))),"milliliters.")
            with open("totalpayment.txt","a") as tp:
                tp.write("\n")
                tp.write("\n")
                tp.write("Type of gasoline : Disel.")
                tp.write("\n")
                tp.write("Price of gasoline : 0.8$ per liter.")
                tp.write("\n")
                tp.write("Purchased : ")
                tp.write(str(dollarsOfGasoline))
                tp.write(" dollars of Disel.")
                tp.write("\n")
                tp.write("\n")
                tp.write("Amount of gasoline is ")
                tp.write(str(int(priceDisel)))
                tp.write(" liters ")
                tp.write(str(int(100 * (priceDisel - int(priceDisel)))))
                tp.write(" milliliters.")
            doYouWantFood()
   
def doYouWantFood():

    with open("foods.txt","r") as foods:
        for food in foods:
            f = food
        hamburgerValue = float(f.split(", ")[0].split(" - ")[1].split(" ")[0])
        sandwichValue = float(f.split(", ")[1].split(" - ")[1].split(" ")[0])
        cheeseburgerValue = float(f.split(", ")[2].split(" - ")[1].split(" ")[0])
        cocacolaValue = float(f.split(", ")[3].split(" - ")[1].split(" ")[0])
        fantaValue = float(f.split(", ")[4].split(" - ")[1].split(" ")[0])
    
    clear()
    yesOrNo = input("\nDo you want to buy food ?\nYes (1) | No (2) : ").strip()
    while True :
        if (yesOrNo == "1"):
            clear()
            with open("foods.txt","r") as tp:
                for x in tp.readlines():
                    a = x
            foodList = a.split(", ")
            showInfoOfFoods = [foodList[0],foodList[1],foodList[2],foodList[3],foodList[4]]
            s()
            for x in showInfoOfFoods:
                print(x)
            s()
            print("Please, enter number with commas (e.g 1,2,3,4,5).")
            choiceOfFoodandDrinking = input("\nWhich food do you want to buy ?\nHamburger (1) | Cheeseburger (2) | Sandwich (3) | Coca-Cola (4) | Fanta (5) : ").split(",")
            s()
            clear()
            s()
            if ("1" in choiceOfFoodandDrinking):
                numberOfHamburgers = int(input("How many hamburgers do you want ?\n- "))
            else:
                numberOfHamburgers = 0
            if ("2" in choiceOfFoodandDrinking):
                numberOfCheeseburgers = int(input("How many cheeseburgers do you want ?\n- "))
            else:
                numberOfCheeseburgers = 0
            if ("3" in choiceOfFoodandDrinking):
                numberOfSandwiches = int(input("How many sandwiches do you want ?\n- "))
            else:
                numberOfSandwiches = 0
            if ("4" in choiceOfFoodandDrinking):
                numberOfCocaColas = int(input("How many Coca-colas do you want ?\n- "))
            else:
                numberOfCocaColas = 0
            if ("5" in choiceOfFoodandDrinking):
                numberOfFantas = int(input("How many Fantas do you want ?\n- "))
            else:
                numberOfFantas = 0
            s()
            clear()
            if (numberOfHamburgers != 0):
                print("Number of hamburgers : ",numberOfHamburgers)
            if (numberOfCheeseburgers != 0):
                print("Number of cheeseburgers : ",numberOfCheeseburgers)
            if (numberOfSandwiches != 0):
                print("Number of sandwiches :",numberOfSandwiches) 
            if (numberOfCocaColas != 0):
                print("Number of Coca-Colas : ",numberOfCocaColas)
            if (numberOfFantas != 0):
                print("Number of Fantas : ",numberOfFantas)

            if ("4" not in choiceOfFoodandDrinking and "5" not in choiceOfFoodandDrinking):
                s()
                clear()
                s()
                drinking = input("Do you want something to drink ?\nYes (1) | No (2) : ")
                while True:
                    if (drinking == "1"):
                        clear()
                        with open("foods.txt","r") as foods:
                            for food in foods:
                                f = food
                            s()
                            print(f.split(", ")[3])
                            print(f.split(", ")[4])
                            choiceOfDrinking = input("\nWhich drinking do you want to buy ?\nCoca-Cola (1) | Fanta (2) : ").split(",")
                            s()
                            if ("1" in choiceOfDrinking):
                                numberOfCocaColas = int(input("How many Coca-Colas do you want ?\n- "))
                            else:
                                numberOfCocaColas = 0
                            if ("2" in choiceOfDrinking):
                                numberOfFantas = int(input("How many Fantas do you want ?\n- "))
                            else:
                                numberOfFantas = 0
                            s()
                            if (numberOfHamburgers != 0):
                                print("Number of hamburgers : ",numberOfHamburgers)
                            if (numberOfCheeseburgers != 0):
                                print("Number of cheeseburgers : ",numberOfCheeseburgers)
                            if (numberOfSandwiches != 0):
                                print("Number of sandwiches :",numberOfSandwiches) 
                            if (numberOfCocaColas != 0):
                                print("Number of Coca-Colas : ",numberOfCocaColas)
                            if (numberOfFantas != 0):
                                print("Number of Fantas : ",numberOfFantas)
                        break

                    elif (drinking == "2"):
                        break

                    else:
                        drinking = int(input("Please, enter 1 (Yes) or 2 (No) : "))     

            priceFoodsAndDrinkings = (hamburgerValue * numberOfHamburgers) + (cheeseburgerValue * numberOfCheeseburgers) + (sandwichValue * numberOfSandwiches) + (cocacolaValue * numberOfCocaColas) + (fantaValue * numberOfFantas)
            clear()
            print("\nThe total amount of goods is",priceFoodsAndDrinkings,"$")

            doYouWantToConfirm = input("\nDo you want to confirm goods ?\nYes (1) | No (2) : ")
            if (doYouWantToConfirm == "1"):
                s()
                clear()
                print("You can take your receipt from \"totalpayment.txt\".")
                with open("totalpayment.txt","a") as tp: 
                    tp.write("\n")
                    if (numberOfHamburgers != 0):
                        tp.write("\n")
                        tp.write("Food name : Hamburger")
                        tp.write("\n")
                        tp.write("Number of purchased hamburgers is ")    
                        tp.write(str(numberOfHamburgers))
                    if (numberOfCheeseburgers != 0):
                        tp.write("\n")
                        tp.write("Food name : Cheeseburger")
                        tp.write("\n")
                        tp.write("Number of purchased cheeseburgers is ")
                        tp.write(str(numberOfCheeseburgers))
                    if (numberOfSandwiches != 0):
                        tp.write("\n")
                        tp.write("Food name : Sandwich")
                        tp.write("\n")
                        tp.write("Number of purchased sandwiches is ")
                        tp.write(str(numberOfSandwiches))
                    if (numberOfCocaColas != 0):
                        tp.write("\n")
                        tp.write("Drinking name : Coca-cola")
                        tp.write("\n")
                        tp.write("Number of purchased Coca-Colas is ")
                        tp.write(str(numberOfCocaColas))
                    if (numberOfFantas != 0):
                        tp.write("\n")
                        tp.write("Drinking name : Fanta")
                        tp.write("\n")
                        tp.write("Number of purchased Fantas is ")
                        tp.write(str(numberOfFantas))
                    tp.write("\n")
                    tp.write("\n")
                    tp.write("Total amount of goods is ")
                    tp.write(str(priceFoodsAndDrinkings))
                    tp.write(" dollars.")
                break
            else:           
                print("\nYou can take your receipt for gasolines from \"totalpayment.txt\".")
                break
            
        elif (yesOrNo == "2"):
            print("\nYou can take your receipt for gasolines from \"totalpayment.txt\".")
            break

        elif (yesOrNo != "1" and yesOrNo != "2"):
            yesOrNo = input("Please, enter 1 (Yes) or 2 (No) : ").strip()
        else:
            yesOrNo = input("Please, enter 1 (Yes) or 2 (No) : ").strip()

def deleteGasolineByName(nameOfGasoline):
    with open("gasolines.txt","r") as gasolines:
        for gasolines in gasolines.readlines():
            g = gasolines
        gasolineList = g.split(", ")

    for x in gasolineList:
        if (x.split(" - ")[0].strip().upper() == nameOfGasoline.upper()):
            gasolineList.remove(x)
            clear()
            s()
            print(nameOfGasoline,"was successfully deleted!")
            s()
            print("Here is the all gasolines.")
            s()
            for y in gasolineList:
                print(y)
            break
    else:
        print("\nThere is no gasoline with this name.")
        
def addGasolineByName(nameOfGasoline, priceOfGasoline):
    with open("gasolines.txt","r") as gasolines:
        for gasolines in gasolines.readlines():
            g = gasolines
        gasolineList = g.split(", ")

    newGasoline=nameOfGasoline+" - "+priceOfGasoline
    
    clear()
    s()
    print("Here is the all gasolines.")
    s()
    gasolineList.append(newGasoline)
    for x in gasolineList:
        print(x)
    
def deleteFoodByName(nameOfFood):
    with open("foods.txt","r") as tp:
        for x in tp.readlines():
            a = x
    foodList = a.split(", ")
    
    for x in foodList:
        if (nameOfFood.upper() == x.split(" - ")[0].strip().upper()):
            foodList.remove(x)
        clear()
        s()
        print(nameOfFood,"was successfully deleted!")
        s()
        print("Here is the all goods.")
        s()
        for y in foodList:
            print(y)

def addFoodByName(nameOfFood, priceOfFood):
    with open("foods.txt","r") as tp:
        for x in tp.readlines():
            a = x
    foodList = a.split(", ")

    newFood=nameOfFood+" - "+priceOfFood+" dollar"

    clear()
    s()
    print("Here is the all foods and drnkings.")
    s()
    foodList.append(newFood)
    for x in foodList:
        print(x)


def permitToMakeChanges():
    clear()
    print("Welcome!")
    select=input("\nPress 1, to see all petrols\nPress 2, to see all foods\nPress 3, to delete gasoline\nPress 4, to add gasoline\nPress 5, to delete food or drinking\nPress 6, to add food or drinking\n-")

    if (select == "1"):
        clear()
        s()
        with open("gasolines.txt","r") as gasolines:
            for gasolines in gasolines.readlines():
                g = gasolines
            gasolineList = g.split(", ")
            showInfoOfGasolines = [gasolineList[0],gasolineList[1],gasolineList[2]]
            for x in showInfoOfGasolines:
                print(x)
    elif (select == "2"):
        clear()
        with open("foods.txt","r") as tp:
            for x in tp.readlines():
                a = x
        foodList = a.split(", ")
        showInfoOfFoods = [foodList[0],foodList[1],foodList[2],foodList[3],foodList[4]]
        s()
        for x in showInfoOfFoods:
            print(x)

    elif (select == "3"):
        clear()
        s()
        nameOfGasoline=input("Enter the name of gasoline : ").upper()
        deleteGasolineByName(nameOfGasoline)

    elif (select == "4"):
        clear()
        s()
        nameOfGasoline=input("Enter the name of gasoline : ")
        priceOfGasoline=input("Enter the price of gasoline : ")
        addGasolineByName(nameOfGasoline, priceOfGasoline)
     
    elif (select == "5"):
        clear()
        s()
        nameOfFood=input("Enter the name of food : ")
        deleteFoodByName(nameOfFood)

    elif (select == "6"):
        clear()
        s()
        nameOfFood=input("Enter the name of food or drinking : ")
        priceOfFood=input("Enter the price of food or drinking : ")
        addFoodByName(nameOfFood, priceOfFood)


def adminCheck():
    adminNameCheck=input("\nEnter your name : ").strip().title()
    adminPasswordCheck=input("Enter your password : ").strip()

    with open("admins.txt","r") as ad:
        for x in ad:
            adminInfo = x
        adminName = adminInfo.split(" - ")[0]
        adminPassword = adminInfo.split(" - ")[1]
        if (adminNameCheck == adminName and adminPassword == adminPasswordCheck):
            permitToMakeChanges()
        else:
            print("\nIncorrect password or username!")

welcome()










































