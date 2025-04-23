def factorial(number):
    result: int = 1
    if number==0 or number==1:
        return 1
    else:
        for i in range(2,number+1):
            result*=i
    return result

if __name__ == "__main__":
    number: int = int(input("Enter a number for which you want to find out the factorial:"))
    answer:int = factorial(number)
    print(answer)