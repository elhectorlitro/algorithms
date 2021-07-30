from random import randint

def Binary_Search(value, numbers, tries, maxi, mini, midi):
    tries+=1
    print("Is it")
    print(midi)
    print("?")
    mid=round(((maxi-mini)/2)+mini)
    if midi == value :
        print("Yes")
        return [mid, tries]
    elif midi > value:
        print("No")
        print(mid)
        Binary_Search(value, numbers, tries, midi, mini,mid)
    else : 
        print("No")
        print(mid)
        Binary_Search(value, numbers, tries, maxi, midi,mid)
    return;

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]#sorted list of int numbers 
to_guess = randint(0,20)
print(to_guess)
to_print = Binary_Search(to_guess, numbers, 0, len(numbers),0,(len(numbers)-0)/2)
print("[Number guessed, number of tries]:")
print(to_print)
