ls = [52,55,85,66,9,70,33,85,91]
for index,i in enumerate(ls):
    if 85==i:
        print("present at index ",index)


min = None
max = None

for i in ls:
    if min is None or i < min:
        min = i
    if max is None or i > max:
        max = i
print("")
print("Minimum: ", min)
print("Maximum: ", max)


print("")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j,end="")
    print(" ")

print(" ")      
for i in range(1, 6):
    for j in range(1, i+1):
        print("*",end="")
    print(" ")
