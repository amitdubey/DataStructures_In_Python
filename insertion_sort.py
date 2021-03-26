from typing import List
def insertionSort(array):
    for i in range(1,len(array)):
        j=i
        while j>0 and array[j]< array[j-1]:
            swap(j,j-1,array)
            j-=1
    return array

def swap(i,j,array):
	array[i],array[j]=array[j],array[i]

def main():
    array =[3,2,1,5,7,9,11,2,4,16]
    print(insertionSort(array))

if __name__=='__main__':
    main()
    