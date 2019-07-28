list=[10, 15, 3, 7]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==17:
            print("True")
            print(i,j)