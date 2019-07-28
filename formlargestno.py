list = ["50", "2", "1", "9"]

for i in range(len(list)):
    for j in range(len(list) - 1):
        if int(list[i][0]) > int(list[j][0]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
largestno = "".join(list)
print(largestno)
