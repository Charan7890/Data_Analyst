# from typing import List

Range:int = int(input("Enter the range(i.e., terminating number such as 10,100,1000..:"))

prime:list[int] = []
for i in range(0,Range+1):
    if i==0 or i==1:
        print(f"{i} is not prime")
    else:
        flag = False
        for j in range(2,i):
            if(i%j==0):
                flag=True
                break
        if flag==False:
            print(f"{i} is prime")
            prime.append(i)
        else:
            print(f"{i} is not prime")
print(prime)

