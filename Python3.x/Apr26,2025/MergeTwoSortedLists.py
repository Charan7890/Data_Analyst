list1: list[int] = [1,2,7,12,15]

list2: list[int] = [5,11,16,23]

# merge two sorted list and the merged list has to be in sorted.

pointer1: int = 0

pointer2: int = 0

mergedList: list[int] = []

while pointer1 < len(list1) and pointer2 < len(list2):
    if list1[pointer1]<list2[pointer2]:
        mergedList.append(list1[pointer1])
        pointer1+=1
    else:
        mergedList.append(list2[pointer2])
        pointer2+=1

while pointer1!=len(list1):
    mergedList.append(list1[pointer1])
    pointer1+=1

while pointer2!=len(list2):
    mergedList.append(list2[pointer2])
    pointer2+=1

print(mergedList)



