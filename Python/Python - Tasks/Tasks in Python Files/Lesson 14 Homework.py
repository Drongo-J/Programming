# SINIFDE YAZILAN PROYEKTE ELAVE OLARAQ , 
#1.QUANTITY YOXLANILSIN, 
#2.DELETE MEHSULU SILMEK
#3.CHANGE ITEM QUANTITY

import os
clear = lambda: os.system('cls')

def s():
    print()

class Product:

    def __init__(self,name,price):
        self.setName(name)
        self.setPrice(price)

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def setName(self,name):
        if (name!=""):
            self.__name=name
        else:
            raise Exception("Please, fill your name.")

    def setPrice(self,price):
        if(price>=0):
            self.__price=price
        else:
            raise Exception("Price should be more than 0.")

    def showInfo(self):
        print("Name of the product : ",self.getName())
        print("Price : ",self.getPrice()," $")


class ProductItem:

    Id=0
    def __init__(self,product,quantity):
        ProductItem.Id+=1
        self.__MyId=ProductItem.Id
        self.product=product
        self.quantity=quantity

    def show(self):
        print("ID : ",self.__MyId)
        self.product.showInfo()

    def getMyId(self):
        return self.__MyId



class Stock:

    def __init__(self,items):
        self.__productItems=items

    def getProductItems(self):
        return self.__productItems

    def addNewItem(self,product,quantity):
        item=ProductItem(product,quantity)
        self.__productItems.append(item)
        print("\"",product.getName(),"\" added successfully!")

    def getProductItemById(self,id):
        for p in self.__productItems:
            if(p.getMyId()==id):
                return p
        raise Exception("\nThere is no item with this ID.")

    def deleteItem(self,id):
        for x in self.__productItems:
            if(x.getMyId()==id):
                self.__productItems.remove(x)
                print("Product removed successfully!")

    def changeQuantity(self,id,quantity):
        for x in self.__productItems:
            if(x.getMyId()==id):
                x.quantity=quantity
                print("Quatity of the product changed successfully!")


    def showAll(self):
        for p in self.__productItems:
            s()
            print("==========================================")
            p.show()
            print("Quantity : ",p.quantity)
            print("==========================================")



class Controller:

    @staticmethod
    def Start():
        p1=Product("GALAXY S21",1899)
        item1=ProductItem(p1,100)

        p2=Product("IPHONE 13 PRO MAX",3500)
        item2=ProductItem(p2,10)

        items=[item1,item2]
        stock=Stock(items)

        print("MAIN MENU")
        print("\nWelcome To The Program!")
        print("\nHere is the all products : ")
        stock.showAll()

        select=input("\nClick 1, to add a new item\nClick 2, to purchase an item\nClick 3, to delete product by ID\nClick 4, to change the quantity of the product\n- ")
        while True:
            if(select=="1"):
                clear()
                s()

                name=input("Enter name of product : ").strip().upper()
                price=float(input("Enter price of product : "))
                product=Product(name,price)
                quantity=int(input("Enter quantity for product : "))

                clear()
                stock.addNewItem(product,quantity)
                print("\nHere is the all products : ")
                stock.showAll()
                break
       

            elif(select=="2"):
                clear()
                s()
            
                id=int(input("Enter product ID : ")) 
                i=0
                for p in items:
                    if(p.getMyId()==id):
                        i+=1
                        break
                if (i==0):
                    raise Exception("There is no product with this ID.")


                quantity=int(input("Enter quantity : "))

                try:
                    productitem=stock.getProductItemById(id)
                    if (productitem.quantity-quantity<0):
                        print("\nThere are no",quantity,"\b",productitem.product.getName().strip(),"\bs in the stock.")
                        break
                    else:
                        productitem.quantity-=quantity
                        clear()
                        print("\"",productitem.product.getName(),"\" sold with this quantity : ",quantity)
                        stock.showAll()
                        break
                except Exception as ex:
                    print("Error : ",ex)

            elif(select=="3"):
                clear()
                s()
                id=int(input("Enter product ID : "))
                i=0
                for p in items:
                    if(p.getMyId()==id):
                        i+=1
                        break
                if (i==0):
                    raise Exception("There is no product with this ID.")

                clear()
                for p in items:
                    if (p.getMyId()==id):
                        s()
                        print("It is the product with the ID",id)
                        s()
                        print("==========================================")
                        p.show()
                        print("Quantity : ",p.quantity)
                        print("==========================================")

                        areYouSure = input("\nAre you sure you want to delete this product?\nYes (1) | No (2) : ")
                        while True:
                            if (areYouSure == "1"):
                                clear()
                                stock.deleteItem(id)
                                print("\nHere is the all products :")   
                                stock.showAll()
                                break
                            elif(areYouSure == "2"):
                                clear()
                                Controller.Start();
                                break
                            elif(areYouSure == ""):
                                areYouSure = input("\nPlease, enter \'Yes\' or \'No\'\nYes (1) | No (2) : ")
                            else:
                                areYouSure = input("\nPlease, enter \'Yes\' or \'No\'\nYes (1) | No (2) : ")

                break    

            elif (select == "4"):
                clear()
                s()
                id=int(input("Enter product ID : "))
                i=0
                for p in items:
                    if(p.getMyId()==id):
                        i+=1
                        break
                if (i==0):
                    raise Exception("There is no product with this ID.")

                for p in items:
                    if (p.getMyId() == id):
                        break
                    else:
                        print("\nThere is no product with this ID.")
                        break


                for p in items:
                    if (p.getMyId()==id):
                        s()
                        print("It is the product with the ID",id)
                        s()
                        print("==========================================")
                        p.show()
                        print("Quantity : ",p.quantity)
                        print("==========================================")
                  
                        quantity=int(input("\nEnter the quantity : "))
                        clear()
                        areYouSure = input("\nAre you sure you want the quantity of this product?\nYes (1) | No (2) : ")
                        while True:
                            if (areYouSure == "1"):
                                clear()
                                stock.changeQuantity(id,quantity) 
                                print("\nHere is the all products :")
                                stock.showAll()
                                break
                            elif(areYouSure == "2"):
                                clear()
                                Controller.Start();
                                break
                            elif(areYouSure == ""):
                                areYouSure = input("\nPlease, enter \'Yes\' or \'No\'\nYes (1) | No (2) : ")
                            else:
                                areYouSure = input("\nPlease, enter \'Yes\' or \'No\'\nYes (1) | No (2) : ")
                break
       
            elif (select==""):
                select=input("Please, enter 1 or 2 or 3 or 4 or 5 : ")

            else:
                select=input("Please, enter 1 or 2 or 3 or 4 or 5 : ")



Controller.Start();


