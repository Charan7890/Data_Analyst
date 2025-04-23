from Factorial import *

def isStrong(number):
    numStore: int = number

    sum: int = 0
    for num in str(number)[::-1]:
        sum += factorial(int(num))

    if sum==numStore:
        return True
        
    else:
        return False
        

if __name__=="__main__":
    number: int = int(input("Enter a number to check whether it's strong or not:"))
    boolvalue: bool = isStrong(number)
    if boolvalue==True:
        print(f"{number} is Strong number")
    else:
        print(f"{number} is not Strong number")





