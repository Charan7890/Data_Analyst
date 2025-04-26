nums: list[int] = [1,2,1,2,1,1,2,4,5,5,12,11]

NonDupElements: list[int] = []

for num in nums:
    if num not in NonDupElements:
        NonDupElements.append(num)
    else:
        continue

print(*NonDupElements)