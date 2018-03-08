# S3C2 Laurel

import datetime

class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title=t
        self.__Author_Artist=a
        self.__ItemID=i
        self.__OnLoan=False
        self.__DueDate=datetime.date.today()
        self.__BorrowerID=0

    def Borrowing(self,n):
        self.__OnLoan=True
        self.__DueDate = self.__DueDate+datetime.timedelta(weeks=3)
        self.__BorrowerID=n

    def PrintDetails(self):
        print(self.__Title,";",self.__Author_Artist,";",end="")
        print(self.__ItemID,";",self.__OnLoan,";")
        print(self.__DueDate,"; Borrower:",self.__BorrowerID)
