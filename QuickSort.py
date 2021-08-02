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
        print("pivot: "+str(compare))
        less = []
        more = []
        pivot_list = []
        for i in range(0,len(unsorted_list)-1):
            if compare < unsorted_list[i]: more.append(unsorted_list[i])
            else : less.append(unsorted_list[i])
        pivot_list.append(pivot)
        print("Lower elements: " + str(less))
        print("Pivot: " + str(pivot_list))
        print("Upper elements: " + str(more))
        return QuickSort(less) + pivot_list + QuickSort(more)

to_sort = GenerateRandomList(2,14,8)
print(to_sort)
print(QuickSort(to_sort))
