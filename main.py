values = list(map(int, input().split(" ")))
print(values)
smallest = []
for i in range(len(values)):
    for j in range(i,len(values)):
        if j == 0:
            smallest = values[j]
        if values[j] < smallest:
            smallest = values[j]
    values[i],values[smallest[1]] = values[smallest[1]],values[i]
    print(values)