# S3C2 Laurel Kuang

1a i

```python
class CustomerRecord:
    def _init_(self):
        self.CustomerID=0
        self.CustomerName=""
        self.TelephoneNumber=""
        self.TotalValue=0
```

1a ii

```python
CustomerData=[CustomerRecord() for i in range(1000)]
```

1b i

```python
def Hash(CustomerID):
    Address=CustomerID%1000
    return Address
```

1b ii

```python
def AddRecord(Customer,CustomerData):
    Address=Hash(Customer.CustomerID)
    while CustomerData[Address].CustomerID!=0:
        Address=Address+1
    CustomerData[Address]=Customer
```

1b iii

```python
def FindRecord(CustomerID,CustomerData):
    Address=Hash(CustomerID)
    while CustomerData[Address].CustomerID!=CustomerID:
        Address=Address+1
    return Address
```

c

```python
import pickle
def StoreData(CustomerData):
    File=open("CustomerData.DAT","wb")
    for i in range(1000):
        pickle.dump(CustomerData[i],File)
    File.close()
```

d

When adding the record, the program should figure out the right record in the random file. When finding the record, the program should read the file first. The program needs to determine the fixed lengths of records before saving them to the random file. 

2

```python
FileName=input("Which file do you want to use?")
try:
    File=open(FileName,"rb")
except:
    print("The file you entered was not found.")
```





