from random import randint

def Binary_Search(value, numbers, tries, maxi, mini):
    tries+=1
    mid=round(((maxi-mini)/2)+mini)
    print("Is it "+str(mid)+"?")
    if mid == value :
        print("Yes")
        return mid, tries
    elif mid > value:
        print("No")
        return Binary_Search(value, numbers, tries, mid, mini)
    else : 
        print("No")
        return Binary_Search(value, numbers, tries, maxi, mid)
    return 0 


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]#sorted list of int numbers 
to_guess = randint(0,20)
print("Number to be guessed: "+str(to_guess))
number_guessed, number_of_tries = Binary_Search(to_guess, numbers, 0, len(numbers),0)
print("Number "+ str(number_guessed)+" after "+str(number_of_tries)+" tries")
