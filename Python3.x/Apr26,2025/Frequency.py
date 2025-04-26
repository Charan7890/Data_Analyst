numbers: list[int] = list(map(int,input("Enter number sequence that will be moved to an array:").strip().split()))

# numbers: list[int] = [2,1,3,5,5,3,3,2,8,7,5]

numSet = set(numbers)

for num in numSet:
    count: int = 0
    for val in numbers:
        if num==val:
            count+=1
    if count==0 or count==1:
        print(f"{num} has been repeated for {count} times")
    else:
        print(f"{num} has been repeated for {count} times")




# print(numbers)