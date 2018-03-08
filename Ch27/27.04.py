#S3C2 Laurel

def PrintDetails(self):
    print("Book Details")
    LibraryItem.PrintDetails(self)
    print(self.__IsRequested)

def PrintDetails(self):
    print("CD Details")
    LibraryItem.PrintDetails(self)
    print(self.__Genre)
