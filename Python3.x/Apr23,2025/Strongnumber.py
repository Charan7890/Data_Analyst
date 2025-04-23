from StrongNumberorNot import *
answer:list[int] = []

def strongfunc(Range):
    for val in range(1,Range+1):
        boolval: bool = isStrong(val)
        if boolval == True:
            answer.append(val)
        else:
            pass

        
if __name__=="__main__":
    Range: int = int(input("Enter a range:"))
    strongfunc(Range)
    print(f"Strong number: {answer}")
