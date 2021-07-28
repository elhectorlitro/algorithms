from random import randint

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]#sorted list of int numbers 
value = randint(0,20) 
tries = 0;    
def Binary_Search(value, numbers, tries): 
  if tries==0:
    low = 0                                                                                                     
    high = len(numbers)                                                                                          
    mid = (high-low/2)                                                                                           
    else:                                                                                                            
      if mid==value:                                                                                                                                                                                                                 
        elif mid < value:
          else :                 
          print("Is the number"+str(mid)+"?")
          print("Number of iteration: "+str(tries)) 
    return;                                                                                                        
  Binary_Search(value, numbers, tries) 
