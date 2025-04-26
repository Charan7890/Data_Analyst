numbers: list[int] = [2,1,3,5,5,3,3,2,8,7,5]

dictionary: dict[int,int] = dict()

for number in numbers:
    if number not in dictionary or dictionary == None:
        dictionary[number] = 1
    else:
        dictionary[number] += 1

# display the result by sorting on thye basis of keys

for val in sorted(dictionary.keys()):
    print(val, dictionary[val], sep= ":", end = "\n")

print(sorted(dictionary.values()))
# print(dictionary)