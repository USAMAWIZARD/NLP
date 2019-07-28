changeavailable = [7, 5, 3, 1]
note = 18
addition = 0
i = 0
while addition != note:
    if (changeavailable[i] + addition <= note):
        addition = changeavailable[i] + addition
        print(changeavailable[i])
    else:
        if i != (len(changeavailable) - 1):
            i += 1
