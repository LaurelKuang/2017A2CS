# S3C2 Laurel Kuang

NullPointer=-1

class TreeNode:
    def _init_(self):
        self.value=""
        self.LeftPointer=NullPointer
        self.RightPointer=NullPointer

    def InitialiseTree():
        BinaryTree=[TreeNode() for i in range(8)]
        RootPointer=NullPointer
        FreeListPointer=0
        for Index in range(7):
            BinaryTree[Index].Right Pointer=Index+1
        return BinaryTree

     def InsertNode(NewItem):
         if FreeListPointer!=NullPointer:
             NewNodePointer=FreeListPointer
             FreeListPointer=BinaryTree[FreePointer].LeftPointer
             BinaryTree[NewNodePointer].value=NewItem
             BinaryTree[NewNodePointer].LeftPointer=NullPointer
             BinaryTree[NewNodePointer].RightPointer=NullPointer
             if RootPointer==NullPointer:
                 RootPointer=NewNodePointer
             else:
                 ThisNodePointer=RootPointer
                 while ThisNodePointer!=NullPointer:
                     PreviousNodePointer=ThisNodePointer
                     if BinaryTree[ThisNodePointer].value>NewItem:
                         TurnedLeft=True
                         ThisNodePointer=BinaryTree[ThisNodePointer].LeftPointer
                     else:
                         TurnedLeft=False
                         ThisNodePointer=BinaryTree[ThisNodePointer].RightPointer
                 if TurnedLeft==True:
                     BinaryTree[PreviousNodePointer].LeftPointer=NewNodePointer
                 else:
                     BinaryTree[PreviousNodePointer].RightPointer=NewNodePointer

     def FindNode(SearchItem):
         ThisNodePointer=RootPointer
         while ThisNodePointer!=NullPointer and BinaryTree[ThisNodePointer].value!=SearchItem:
             if BinaryTree[ThisNodePointer].value>SearchItem:
                 ThisNodePointer=BinaryTree[ThisNodePointer].LeftPointer
             else:
                 ThisNodePointer=BinaryTree[ThisNodePointer].RightPointer
         return ThisNodePointer
             






     
