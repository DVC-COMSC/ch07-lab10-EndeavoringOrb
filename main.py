values = list(map(int, input().split(" ")))
print(values)
for i in range(len(values)):
    smallest = 0
    for j in range(0,len(values)-i):
        current_index = i+j
        if smallest == 0:
            smallest = values[current_index]
            ind = current_index
        if values[current_index] < smallest:
            smallest = values[current_index]
            ind = current_index
    values[i],values[ind] = values[ind],values[i]
    print(values)