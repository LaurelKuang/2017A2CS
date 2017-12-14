# S3C2 Laurel Kuang

def BubbleSort(List):
    while len(List)>0:
        for i in range(len(List)-1):
            if List[i]>List[i+1]:
                List[i],List[i+1]=List[i+1],List[i]
        len(List)=len(List)-1
    return List
