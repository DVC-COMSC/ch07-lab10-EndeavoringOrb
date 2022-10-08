values = list(map(int, input().split(" ")))
smallest = []
for i in range(len(values)):
    for j in range(i,len(values)):
        if len(values[j]) < len(smallest):
            smallest = [values[j],i+j]
    values[i],values[smallest[1]] = values[smallest[1]],values[i]