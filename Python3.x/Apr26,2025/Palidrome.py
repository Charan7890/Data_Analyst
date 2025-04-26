string: str = input("Enter a string:").strip().lower()

if string == string[::-1]:
    print("Palindrome: "+string)
else:
    print("Not palindrome: "+string)