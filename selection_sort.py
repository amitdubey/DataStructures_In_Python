from typing import List
def selectionSort(array):
    currentidx =0 
    while currentidx < len(array)-1:
        smallidx = currentidx
        for i in range(currentidx+1, len(array)):
            if array[smallidx] > array[i]:
                smallidx =i
        swap(currentidx,smallidx,array)
        currentidx+=1
    return array

def swap(i,j,array):
	array[i], array[j]=array[j], array[i]
			

def main():
    array =[3,2,1,5,7,9,11,2,4,16]
    print(selectionSort(array))

if __name__=='__main__':
    main()
    