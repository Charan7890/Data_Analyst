string: str = input("Enter a string:").strip().lower()

length: int = len(string)//2

i: int = 0
j: int = len(string)-1
flag: bool = False

while i<j:
    if string[i]!=string[j]:
        flag = True
        break
    else:
        i+=1
        j-=1

if flag == True:
    print(f"{string} is not palindrome")
else:
    print(f"{string} is palindrome")