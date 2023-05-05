#Car => id,model,vendor,Engine,hasSpoiler(bu mashina aid ozellikdi)
#Ship => id,model,vendor,Engine,hasSail(sail - yelkən)
#Airplane => id,model,vendor,Engine,engineCount,passengersCapacity

#Engine=>engine_no,company,volume

#=> ishare klas oldugunu bildirir
#Bu klaslar arasinda Inheritance elaqesi yaradilsin,
#her bir klasda show methodu yazilsin

#VehicleDepo=[cars,ships,airplanes]

#def addCar(car):
#	cars.append(car)




class Engine:
    def __init__(self, engine_no,company,volume):
        self.set_engine_no(engine_no)
        self.set_company(company)
        self.set_volume(volume)

    def set_engine_no(self, engine_no):
        if (engine_no != ""):
            self.__engine_no = engine_no
        else:
            raise Exception("Engine number must be filled in!")

    def set_company(self, company):
        if (company != ""):
            self.__company = company
        else:
            raise Exception("Company must be filled in!")
    
    def set_volume(self, volume):
        if (int(volume) > 0):
            self.__volume = volume
        else:
            raise Exception("Value must be greater than zero!")
        if (volume != ""):
            self.__volume = volume
        else:
            raise Exception("Volume must be filled in!")


    def get_engine_no(self):
        return self.__engine_no

    def get_company(self):
        return self.__company

    def get_volume(self):
        return self.__volume

    def show_info_of_engine(self):
        print("Engine number : ",self.get_engine_no())
        print("Company of engine : ",self.get_company())
        print("Volume of engine : ",self.get_volume())  


class Car(Engine):
    cars=[]
    def __init__(self, id, model, vendor, has_spoiler, engine_no, company, volume):
        super().__init__(engine_no, company, volume)
        self.set_id(id)
        self.set_model(model)
        self.set_vendor(vendor)
        self.set_has_spoiler(has_spoiler)

    def set_id(self, id):
        if (id != ""):
            self.__id = id
        else:
            raise Exception("Vehicle Identification Number (ID) must be filled in!")

    def set_model(self, model):
        if (model != ""):
            self.__model = model
        else:
            raise Exception("Model must be filled in!")

    def set_vendor(self, vendor):
        if (vendor != ""):
            self.__vendor = vendor
        else:
            raise Exception("Vendor must be filled in!")

    def set_has_spoiler(self, has_spoiler):
        if (has_spoiler != ""):
            self.__has_spoiler = has_spoiler
        else:
            raise Exception("\"Does car have a spoiler?\" must be filled in!")

    def get_id(self):
        return self.__id

    def get_model(self):
        return self.__model

    def get_vendor(self):
        return self.__vendor

    def get_has_spoiler(self):
        return self.__has_spoiler

    def add_car(self,car):
        cars.append(car)

    def show_vehicle(self):
        print("==================================================================")
        print("Vehicle Identification Number (ID) of the car : ",self.get_id())
        print("Model of the car : ",self.get_model())
        print("Vendor of the car : ",self.get_vendor())
        print("Does car have a spoiler? : ",self.get_has_spoiler())
        super().show_info_of_engine()
        print("==================================================================")


class Ship(Engine):
    def __init__(self, id, model, vendor, has_sail, engine_no, company, volume):
        super().__init__(engine_no, company, volume)
        self.set_id(id)
        self.set_model(model)
        self.set_vendor(vendor)
        self.set_has_sail(has_sail)

    def set_id(self, id):
        if (id != ""):
            self.__id = id
        else:
            raise Exception("Vehicle Identification Number (ID) must be filled in!")

    def set_model(self, model):
        if (model != ""):
            self.__model = model
        else:
            raise Exception("Model must be filled in!")

    def set_vendor(self, vendor):
        if (vendor != ""):
            self.__vendor = vendor
        else:
            raise Exception("Vendor must be filled in!")

    def set_has_sail(self, has_sail):
        if (has_sail != ""):
            self.__has_sail = has_sail
        else:
            raise Exception("\"Does car have a sail?\" must be filled in!")

    def get_id(self):
        return self.__id

    def get_model(self):
        return self.__model

    def get_vendor(self):
        return self.__vendor

    def get_has_sail(self):
        return self.__has_sail

    def show_vehicle(self):
        print("==================================================================")
        print("Vehicle Identification Number (ID) of the ship : ",self.get_id())
        print("Model of the ship : ",self.get_model())
        print("Vendor of the ship : ",self.get_vendor())
        print("Does ship have a sail? : ",self.get_has_sail())
        super().show_info_of_engine()
        print("==================================================================")


class Plane(Engine):
    def __init__(self, id, model, vendor, engine_count, passengers_capacity, engine_no, company, volume):
        super().__init__(engine_no, company, volume)
        self.set_id(id)
        self.set_model(model)
        self.set_vendor(vendor)
        self.set_engine_count(engine_count)
        self.set_passengers_capacity(passengers_capacity)

    def set_id(self, id):
        if (id != " "):
            self.__id = id
        else:
            raise Exception("Vehicle Identification Number (ID) must be filled in!")

    def set_model(self, model):
        if (model != ""):
            self.__model = model
        else:
            raise Exception("Model must be filled in!")

    def set_vendor(self, vendor):
        if (vendor != ""):
            self.__vendor = vendor
        else:
            raise Exception("Vendor must be filled in!")

    def set_engine_count(self, engine_count):
        if (engine_count > 0):
            self.__engine_count = engine_count
        else:
            raise Exception("Engine count can't be less thn zero or zero!")

    def set_passengers_capacity(self, passengers_capacity):
        if (passengers_capacity > 0):
            self.__passengers_capacity = passengers_capacity
        else:
            raise Exception("Passenger capacity can't be less thn zero or zero!")

    def get_id(self):
        return self.__id

    def get_model(self):
        return self.__model

    def get_vendor(self):
        return self.__vendor

    def get_engine_count(self):
        return self.__engine_count

    def get_passengers_capacity(self):
        return self.__passengers_capacity

    def show_vehicle(self):
        print("==================================================================")
        print("Vehicle Identification Number (ID) of the plane : ",self.get_id())
        print("Model of the plane : ",self.get_model())
        print("Vendor of the plane : ",self.get_vendor())
        print("Engine count : ",self.get_engine_count())
        print("Passengers capacity : ",self.get_passengers_capacity())
        super().show_info_of_engine()
        print("==================================================================")



#Task 1

#try:
#    car1=Car("PJ12345U123456P","Toyota","John Johnlu","Yes",2488152,"Blackstone",3.5)
#    car1.show_vehicle()

#    ship1=Ship("WBAFR7C57CC811956","HMY ROYAL CAROLINE","Tural Turallı","Yes",2378237,"MTU Marine Diesel Engine",15)
#    ship1.show_vehicle()

#    plane1=Plane("RE34126P894593E","Boeing","Məmməd Məmmədli",6,99,3674093,"General Electric",55)
#    plane1.show_vehicle()
#except Exception as ex:
#    print("Exception : ",ex)


#Task 2

#car1=Car("PJ12345U123456P","Toyota","John Johnlu","Yes",2488152,"Blackstone",3.5)
#ship1=Ship("WBAFR7C57CC811956","HMY ROYAL CAROLINE","Tural Turallı","Yes",2378237,"MTU Marine Diesel Engine",15)
#plane1=Plane("RE34126P894593E","Boeing","Məmməd Məmmədli",6,99,3674093,"General Electric",55)
#VehicleDepo=[car1,ship1,plane1]

#for x in VehicleDepo:
#    print(x.show_vehicle())


