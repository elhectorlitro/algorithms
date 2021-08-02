import random 

def GenerateRandomList(Mini,Maxi,Num_of_elements):
   ran_list=[]
   for i in range(0,Num_of_elements):
       ran_list.append(random.randint(Mini,Maxi))
   return ran_list

def QuickSort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    else :
        pivot = int(len(unsorted_list)/2)
        compare = unsorted_list[pivot]
        less = []
        more = []
        pivot_list = []
        for i in range(0,len(unsorted_list)):
            if compare < unsorted_list[i] and i != pivot:
                more.append(unsorted_list[i])
            elif compare >= unsorted_list[i] and i != pivot:
                less.append(unsorted_list[i])
            else : 
                pivot_list.append(compare)
        return QuickSort(less) + QuickSort(pivot_list) + QuickSort(more)
print("Type the minimum value of the random list you want to create: ")
Min = int(input())
print("Type the maximum value of the random list you want to create: ")
Max = int(input())
print("Type the number of the elements for the random list you want to create: ")
Num = int(input())
to_sort = GenerateRandomList(Min,Max,Num)
print("Unsorted list: " + str(to_sort))
print("Sorted list: " + str(QuickSort(to_sort)))
