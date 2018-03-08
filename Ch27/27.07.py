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


import datetime

class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title=t
        self.__Author_Artist=a
        self.__ItemID=i
        self.__OnLoan=False
        self.__DueDate=datetime.date.today()
        self.__BorrowerID=0

    def GetTitle(self):
        return(self.__Title)

    def GetAuthor_Artist(self):
        return(self.__Author_Artist)

    def GetItemID(self):
        return(self.__ItemID)

    def GetOnLoan(self):
        return(self.__OnLoan)

    def GetDueDate(self):
        return(self.__DueDate)

    def GetBorrowerID(self):
        return(self.__BorrowerID)
    
    def Borrowing(self,n):
        self.__OnLoan=True
        self.__DueDate = self.__DueDate+datetime.timedelta(weeks=3)
        self.__BorrowerID=n

    def Returning(self):
        self.__OnLoan=False
    
    def PrintDetails(self):
        print(self.__Title,";",self.__Author_Artist,";",end="")
        print(self.__ItemID,";",self.__OnLoan,";")
        print(self.__DueDate,";",self.__BorrowerID)


class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False
        self.__RequestedBy=0

    def GetIsRequested(self):
        return(self.__IsRequested)

    def GetRequestedBy(self):
        return(self.__RequestedBy)

    def SetIsRequested(self,n):
        self.__IsRequested=True
        self.__RequestedBy=n

    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested,';',self.__RequestedBy)


class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre=""

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self,g):
        self.__Genre=g

    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print(self.__Genre)

def Menu():
    print("1 - Add a new borrower")
    print("2 - Add a new book")
    print("3 - Add a new CD")
    print("4 - Borrow book")
    print("5 - Return book")
    print("6 - Borrow CD")
    print("7 - Return CD")
    print("8 - Request book")
    print("9 - Print all details")
    print("99 - Exit program")
    print("Enter your menu choice: ")


def Main():
    Finish=False
    while Finish==False:
        Menu()
        Choice=int(input())
        if MenuChoice==1:
            BorrowerName=input("Name: ")
            Email=input("Email address: ");
            BorrowerID=0
            NextBorrowerID+=1
            Borrower=Borrower(BorrowerName, Email, BorrowerID)
        elif MenuChoice==2:
            Title=input("Title: ")
            Author=input("Author: ")
            ItemID=0
            NextBookID+=1
            Book=TBook(Title, Author, ItemID)
        elif MenuChoice==3:
            Title=input("Title: ")
            Artist=input("Artist: ")
            ItemID=0
            NextCDID+=1
            CD=CD(Title, Artist, ItemID)
        elif MenuChoice==4:
            BorrowerID=input("Borrower ID: ")
            ItemID=input("Book ID: ")
            Book.Borrowing(ItemID, Borrower)
        elif MenuChoice==5:
            BorrowerID=input("Borrower ID: ")
            ItemID=input("Book ID: ")
            Book.Returning(ItemID, Borrower)
        elif MenuChoice==6:
            BorrowerID=input("Borrower ID: ")
            ItemID=input("CD ID: ")
            CD.Borrowing(ItemID, Borrower)
        elif MenuChoice==7:
            BorrowerID=input("Borrower ID: ")
            ItemID=input("CD ID: ")
            CD.Returning(ItemID, Borrower)
        elif MenuChoice==8:
            BorrowerID=input("Borrower ID: ")
            ItemID=input("Book ID: ")
            Book.RequestBook(ItemID, Borrower)
        elif MenuChoice==9:
            print("Borrower Details")
            Borrower.printDetails()
            print("Book Details")
            Book.printDetails()
            print("CD Details")
            CD.printDetails()
        elif MenuChoice == 99:
            Finish = True
        else:
            print("Invalid input")
    input()


Main()

    

        
