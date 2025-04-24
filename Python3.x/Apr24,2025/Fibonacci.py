Range: int = int(input("Enter the no.of terms you require from Fibonacci:"))

fib: list[int] = []

first: int = 0

second: int = 1
fib.extend([first,second])

if Range==0:
    print("no terms has been selected fro series")
elif Range == 1:
    print("Term:["+ str(0)+"]")
elif Range == 2:
    print("Terms:["+ str(0)+ ", "+str(1)+"]")
else:
    for _ in range(3,Range+1):
        third: int = first + second
        fib.append(third)
        first = second
        second = third
    print(f"Terms: {fib}")

