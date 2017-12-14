# S3C2 Laurel Kuang

NullPointer=-1

class StackNode:
    def __init__(self):
        self.value=""
        self.nextP=NullPointer

class Stack:
    def __init__(self,length):
        self.tp=NullPointer
        self.fp=0
        self.records=[]
        for i in range(length):
            NewNode=StackNode()
            NewNode.nextpointer=i+1
            self.records.append(NewNode)
        NewNode.nextpointer=-1
        
    def push(self,Item):
        if self.fp!=NullPointer:
            self.newnullpointer=self.fp
            self.records[self.newnullpointer].value=Item
            self.fp=self.records[self.fp].nextpointer
            self.records[self.newnullpointer].nextpointer=self.tp
            self.tp=self.newnullpointer
        else:
            print("No space available.")
            
    def pop(self):
        if self.tp==NullPointer:
            print("No data.")
            return("")
        else:
            value=self.records[self.tp].value
            self.cNodeP=self.tp
            self.tp=self.records[self.tp].nextpointer
            self.records[self.cNodeP].nextpointer=self.fp
            self.fp=self.cNodeP
            return(value)

