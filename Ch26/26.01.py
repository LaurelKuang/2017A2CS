#S3C2 Laurel 

class CarRecord:
    def _init_(self):
        self.VehicleID=""
        self.Registration=""
        self.DateOfRegistration=None
        self.EngineSize=0
        self.PurchasePrice=0.00

import pickle

def Write():
    CarFile=open("Cars.DAT", "wb")
    for i in range(5):
        pickle.dump(Car[i],CarFile)
    CarFile.close()

def Load():
    CarFile=open("Cars.DAT", "rb")
while True:
    Car.append(pickle.load(CarFile)) 
CarFile.close()

def Output():
    for i in range(5):
        print(Car[i].VehicleID,Car[i].Registration,Car[i].DateOfRegistration,Car[i].EngineSize,Car[i].PurchasePrice)

def Main():
    for i in range(5):
        ThisCar=CarRecord()
        ThisCar.VehicleID=input("What is the vehicle ID?")
        ThisCar.Registration=input("What is the Registration?")
        ThisCar.DateOfRegistration=input("What is the date of registration?")
        ThisCar.EngineSize=input("What is the engine size?")
        ThisCar.PurchasePrice=input("What is the purchase price?")
        Car.append(ThisCar)
    Write()
    Load()
    Output()
    
Main()
