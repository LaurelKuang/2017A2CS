# S3C2 Laurel Kuang

def BinarySearch(List,SearchItem):
    Found=False
    SearchFailed=False
    First=0
    Last=len(List)-1
    while not Found and not SearchFailed:
        Middle=(First+Last)//2
        if List[Middle]==SearchItem:
            Found=True
        else:
            if First>=Last:
                SearchFailed=True
            else:
                if List[Middle]>SearchItem:
                    Last=Middle-1
                else:
                    First=Middle+1
    if Found==True:
        print(Middle)
    else:
        print("Item not present in array.")
