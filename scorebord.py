scorearray = [100, 100, 50, 40, 40, 20, 10]
alicescore = [5, 25, 50, 120]
appendednewheighscore = scorearray

for i in alicescore:
    appendednewheighscore.append(i)
    appendednewheighscore.sort(reverse=True)
    nonrep = list(set(appendednewheighscore))
    nonrep.sort(reverse=True)
    print(nonrep.index(i) + 1)
    appendednewheighscore.remove(i)
