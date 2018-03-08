# S3C2 Laurel

class Borrower():
    def __init__(self,n,e,b):
        self.__BorrowerName=n
        self.__EmailAddress=e
        self.__BorrowerID=b
        self.__ItemsOnLoan=0

    def GetBorrowerName(self):
        return(self.__BorrowerName)

    def GetEmailAddress(self):
        return(self.__EmailAddress)

    def GetBorrowerID(self):
        return(self.__BorrowerID)

    def GetItemsOnLoan(self):
        return(self.__ItemsOnLoan)

    def UpdateItemsOnLoan(self,m):
        self.__ItemsOnLoan+=m

    def PrintDetails(self):
        print("Borrower's name:",self.__BorrowerName)
        print("Email address:",self.__EmailAddress)
        print("ID:",self.__BorrowerID)
        print("Items on loan:",self.__ItemsOnLoan)

    def main():
        NewBorrower=Borrower("Laurel","Laurel@gmail.com","0321")
        NewBorrower.UpdateItemsOnLoan(5)
        NewBorrower.PrintDetails()
        
