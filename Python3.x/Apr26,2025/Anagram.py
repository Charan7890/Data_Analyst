string1: str = input("enter first name:").strip().lower()

string2: str = input("enter second name:").strip().lower()

string1: list[str] = list(string1)

string2: list[str] = list(string2)

string1.sort()
string2.sort()

if string1 == string2:
    print("Anagram")
else:
    print(f"Not anagram")

