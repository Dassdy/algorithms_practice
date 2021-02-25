
def swapNodes(nodeA, nodeB):
    nodeA, nodeB=nodeB, nodeA

def heepAdjust(arrayToSort, start):
    i=start
    while 2*i<len(arrayToSort)-1 and 2*i+1 <= len(arrayToSort)-1:
        temp = arrayToSort[i]
        if arrayToSort[2*i] < arrayToSort[2*i+1]:
            if arrayToSort[i] < arrayToSort[2*i+1]:
                arrayToSort[i]=arrayToSort[2*i+1]
                arrayToSort[2*i+1]=temp
                i=2*i+1
        else:
            if arrayToSort[i] < arrayToSort[2*i]:
                arrayToSort[i]=arrayToSort[2*i]
                arrayToSort[2*i]=temp
                i=2*i
    if 2*i==len(arrayToSort)-1:
        temp = arrayToSort[i]
        if arrayToSort[i] < arrayToSort[2*i]:
            arrayToSort[i]=arrayToSort[2*i]
            arrayToSort[2*i]=temp

def heepSort(arrayToSort):

    if len(arrayToSort)<2:
        pass
    else:
        arrayToSort.append(0)
        for i in range(0, int((len(arrayToSort)-1)/2)):
            heepAdjust(arrayToSort, int((len(arrayToSort)-1)/2-i))
        lengthOfInit=len(arrayToSort)
        for i in range(1, len(arrayToSort)):
            swapNodes(arrayToSort[i],arrayToSort[-1])
            heepAdjust(arrayToSort[0,lengthOfInit-i], int((lengthOfInit-1)/2-i))
            

    return arrayToSort


def main():
    L = [50, 16, 30, 10, 60,  90,  2, 80, 70]
    print(heepSort(L))


if __name__ == '__main__':
    main()