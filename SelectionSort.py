import random

def GenerateRandomList(Mini, Maxi, Num_of_elements):
  ran_list = []
  for i in range (0,Num_of_elements):
      ran_value = random.randint(Mini,Maxi)
      ran_list.append(ran_value)
  return ran_list

def SelectionSort(unsorted_list):#Only works with positive numbers
  sorted_list=[]
  while (len(sorted_list)<len(unsorted_list)) :
      current_max = 0
      over=0
      for i in range(len(unsorted_list)):
        if unsorted_list[i] > current_max:
            current_max = unsorted_list[i]
            over = i
      sorted_list.append(current_max)
      unsorted_list[over]=-1
  return sorted_list
print("Enter the lower limit for the random list values: ")
Min = int(input())
print("Enter the upper limit for the random list values: ")
Max = int(input())
print("Enter the number of elements for the random list: ")
Num = int(input())
List = GenerateRandomList(Min, Max, Num)
print("Here is your random list before sorting: ")
print(List)
SortedList = SelectionSort(List)
print("Here is your random list after sorting: ")
print(SortedList)


