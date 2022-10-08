values = list(map(int, input().split(" ")))
smallest = []
for i in range(len(values)):
    for j in range(i,len(values)):
        if values[j] < smallest:
            smallest = [values[j],i+j]
    values[i],values[smallest[1]] = values[smallest[1]],values[i]