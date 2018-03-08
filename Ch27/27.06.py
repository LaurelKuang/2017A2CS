# S3C2 Laurel


class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False
        self.__RequestedBy=0

    def GetIsRequested(self):
        return(self.__IsRequested)

    def SetIsRequested(self,n):
        self.__IsRequested=True
        self.__RequestedBy=n
