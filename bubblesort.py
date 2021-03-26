from typing import List

def bubble_sort(our_list):
        has_swapped = True
        num_of_iterations = 0
        while(has_swapped):
            has_swapped = False
            for i in range(len(our_list) - num_of_iterations - 1):
                if our_list[i] > our_list[i+1]:
                # Swap
                    our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
            num_of_iterations += 1
        return our_list
    

def main():
    array =[3,2,1,5,7,9,11,2,4,16]
    print(bubble_sort(array))

if __name__=='__main__':
    main()
    

 