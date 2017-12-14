# S3C2 Laurel Kuang

class HashTable:
    def __init__(self,size):
        self.size=size
        self.HashTable=[None]*size

    def Hash(Key):
        Address=Key%(n+1)
        return Address

    def Insert(NewRecord):
        Index=Hash(NewRecord.Key)
        while HashTable[Index]!=None:
            Index=Index+1
            if Index>10:
                Index=1
        HashTable[Index]=NewRecord

    def FindRecord(SearchKey):
        Index=Hash(SearchKey)
        while HashTable[Index].Key!=SearchKey and HashTable[Index]!=None:
            Index=Index+1
            if Index>10:
                Index=0
        if HashTable[Index]!=None:
            return HashTable[Index]
