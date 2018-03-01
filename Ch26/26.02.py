#S3C2 Laurel

class CarRecord:
    def _init_(self):
        self.VehicleID=""
        self.Registration=""
        self.DateOfRegistration=None
        self.EngineSize=0
        self.PurchasePrice=0.00

import pickle

def Input():
    ThisCar=CarRecord()
    ThisCar.VehicleID=input("What is the vehicle ID?")
    ThisCar.Registration=input("What is the Registration?")
    ThisCar.DateOfRegistration=input("What is the date of registration?")
    ThisCar.EngineSize=input("What is the engine size?")
    ThisCar.PurchasePrice=input("What is the purchase price?")
    return ThisCar

def Initialise():
    Size=30
    CarFile=open("Cars.DAT","wb")
    for i in range(50):
        Address=i*Size+1
        Cars.seek(Address)
        pickle.dump(CarRecord(),Cars)
    Cars.close()

def Save(ThisCar):
    Address=Hash(ThisCar.VehicleID)
    Cars.seek(Address)
    pickle.dump(ThisCar,Cars)

def Find(ThisCar.VehicleID):
    Address=Hash(ThisCar.VehicleID)
    Cars.seek(Address)
    ThisCar=pickle.load(Cars)
    return ThisCar

def Output(ThisCar):
    print("Registration:",ThisCar.Registration)
    print("DateOfRegistration:",ThisCar.Registration)
    print("EngineSize:",ThisCar.EngineSize)
    print("PurchasePrice:",ThisCar.PurchasePrice)


ThisCar=CarRecord()
Initialise()
CarFile=open("Cars.DAT","wb+")

Answer=input("Are you going to add a record? Please enter yes or no.")
while Answer=="yes":
    ThisCar=CarRecord()
    ThisCar=Input()
    Save(ThisCar)
    Answer=input("Are you going to add a record? Please enter yes or no.")

Answer=input("Are you going to find a record? Please enter yes or no.")
while Answer=="yes":
    ThisCar.VehicleID=input("Please enter VehicleID.")
    ThisCar=Find(ThisCar.VehicleID)
    Output(ThisCar)
    Answer=input("Are you going to find a record? Please enter yes or no.")
    
Cars.close()




    



    
