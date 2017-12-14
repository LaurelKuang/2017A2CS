# S3C2 Laurel Kuang

NullPointer=-1

class QueueNode:
    def __init__(self):
        self.value=""
        self.nextP=NullPointer

class Queue:
    def __init__(length):
        Queue=[QueueNode() for i in range(5)]
        head=NullPointer
        end=NullPointer
        freelistpointer=0
        records=[]
        for i in range(4):
            Queue[Index].pointer=Index+1
            Queue[4].pointer=NullPointer

    def Enqueue(self,Item):
        if self.freelistpointer!=NullPointer:
            self.newnp=self.freelistpointer
            self.records[self.newnp].value=Item
            self.freelistpointer=self.records[self.freelistpointer].nextPointer
            self.records[self.newnp].nextPointer=NullPointer
            if self.ep==NullPointer:
                self.sp=self.newnp
            else:
                self.records[self.ep].nextPointer=self.newnp
            self.ep=self.newnp
            
        else:
            print("There is no space available")

    def Dequeue(self):
        if self.sp==NullPointer:
            print("No data")
            return("")
        else:
            tempValue=self.records[self.sp].value
            tempPointer=self.records[self.sp].nextPointer
            if tempPointer==NullPointer:
                self.ep=NullPointer
            self.records[self.sp].nextPointer=self.freelistpointer
            self.freelistpointer=self.sp
            self.sp=tempPointer
        return(self.records[self.freelistpointer].value) 
