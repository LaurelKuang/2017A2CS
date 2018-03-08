# S3C2 Laurel

import datetime

class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title=t
        self.__Author_Artist=a
        self.__ItemID=i
        self.__OnLoan=False
        self.__DueDate=datetime.date.today()

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

    def Borrowing(self):
        self.__OnLoan=True
        self.__DueDate = self.__DueDate+datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan=False

    def PrintDetails(self):
        print(self.__Title,";",self.__Author_Artist,";",end="")
        print(self.__ItemID,";",self.__OnLoan,";",self.__DueDate)


class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False
        self.__RequestedBy=0

    def GetIsRequested(self):
        return(self.__IsRequested)

    def SetIsRequested(self):
        self.__IsRequested=True

class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre=""

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self,g):
        self.__Genre=g



C=[]
C.append(CD('And Justice For All','Metallica',321))
C.append(CD('Dark Side Of The Moon','Pink Floyd',654))
C.append(CD('Black Sabbath','Black Sabbath',987))
C.append(CD('Hello','Laurel',921))
C.append(CD('Bright','Jenny',543))
B=[]
B.append(Book('12 Rules for Life','Jordan Peterson',876))
B.append(Book('White Fang','Jack London',931))
B.append(Book('Mathematics','Tom',534))
B.append(Book('Computer Science','John',678))
for i in C:
    i.PrintDetails()
for i in B:
    i.PrintDetails()



        
