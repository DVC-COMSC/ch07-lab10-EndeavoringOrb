values = list(map(int, input().split(" ")))
print(values)
smallest = []
for i in range(len(values)):
    for j in range(i,len(values)):
        if j == 0:
            smallest = values[j]
            ind = j
        if values[j] < smallest:
            smallest = values[j]
            ind = j
    values[i],values[ind] = values[ind],values[i]
    print(values)