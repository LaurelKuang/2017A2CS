# Chapter 27 Exam Style Questions

S3C2 Laurel Kuang



1a

​                           BankAccount

​                                    ⬆

​            I                                               I

PersonalAccount                SavingsAccount



1b

```python
class BankAccount:
    def __init__(self,m):
        self.__AccountHolderName=""
        self.__IBAN=m
        
    def SetAccountHolderName(self,n):
        self.__AccountHolderName=n
        
    def GetAccountHolderName(self):
        return(self.__AccountHolderName)
    
    def GetIBAN(self):
        return(self.__IBAN)
```



1c i

Attributes: MonthlyFee, AgreedOverdraftLimit

Methods: Consturctor, SeAgreedtOverDraftLimit, GetAgreedOverDraftLimit, GetMonthlyFee



1c ii

Attributes: Interest, AgreedInterestRate

Methods: Consturctor, SetAgreedInterestRate, GetAgreedInterestRate, GetInterest



1c iii

Encapsulation



2a

SeasonTicketHolder

PRIVATE

TicketHolderName: STRING

EmailAddress : STRING

PUBLIC

Constructor()

GetTicketHolderName()

GetEmailAddress()



Pay-As-You-Go-TicketHolder

PRIVATE

Amount : CURRENCY

PUBLIC

Constructor(Name: STRING, email : STRING)

GetAmount()

UpdateAmount()



ContractTicketHolder

PRIVATE

MonthlyFee : CURRENCY

PUBLIC

Constructor(Name: STRING, email : STRING, Fee : CURRENCY)

GetFee()



2b i

Because the SeasonTicketHolder attributes should only be altered by the class methods.



2b ii

Because the SeasonTicketHolder methods should be used to access attributes.



2c

```python
NewCustomer=ContractTicketHolder("A.Smith","xyz@abc.xx",10)
```



3a

Containment



3b

```python
class NodeClass :
    def __init__(self):
        self.__Data=""
        self.__Pointer=-1
    
    def SetData(self, d):
        self.__Data=d
    
    def GetData(self):
        return(self.__Data)
    
    def SetPointer(self, x):
        self.__Data=x
        
     def GetPointer(self):
        return(self.__Pointer)
```



3c

```python
class QueueClass :
    def __init__(self):
        self.__Queue=[NodeClass() for i in range(51)]
        self.__Head=-1
        self.__Tail=-1
```



3d

```python
def JoinQueue(self, d):
    if Head==-1 :
        Head=0
    self.__Tail+=1 
    i=self.__Tail
    self.__Queue[i].SetData(d)
```