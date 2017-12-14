#S3C2 Laurel Kuang

NullPointer=-1

class ListNode:
    def __init__(self):
        self.value=''
        self.nextpointer=NullPointer

class List:
    def __init__(self,length):
        self.freeP=0
        self.sp=-1
        self.records=[]
        for i in range(length):
            NewNode=ListNode()
            NewNode.nextpointer=i+1
            self.records.append(NewNode)
        NewNode.nextpointer=NullPointer
    
    def Access(self):
        self.cp=self.sp
        while self.cp != NullPointer:
            print(self.records[self.cp].value)
            self.cp=self.records[self.cp].nextpointer

    def Find(self,Item):
        self.cNodeP=self.sp
        while self.cNodeP != NullPointer and self.records[self.cNodeP].value != Item:
            self.cNodeP=self.records[self.cNodeP].nextpointer
        return self.cNodeP

    def Delete(self,Item):
        self.cNodeP=self.sp
        while self.cNodeP != NullPointer and self.records[self.cNodeP].value != Item:
            self.prevNodeP=self.cNodeP
            self.cNodeP=self.records[self.cNodeP].nextpointer
        if self.cNodeP != NullPointer:
            if self.cNodeP ==self.sp:
                self.sp=self.records[self.sp].nextpointer
            else:
                self.records[self.prevNodeP].nextpointer=self.records[self.cNodeP].nextpointer
            self.records[self.cNodeP].nextpointer=self.freeP
            self.freeP=self.cNodeP

