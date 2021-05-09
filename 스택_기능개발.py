def solution(progresses, speeds):
    ap = []
    answer= []
    for prog, spe in zip(progresses, speeds):
        c = 0
        while prog < 100:
            c += 1
            prog += spe
        ap.append(c)
    while len(ap) != 0:
        count = 1
        ids = ap[0]
        lst = ap[1:]
        del ap[0]
        for j in lst:
            if ids>=j:
                count += 1
                del ap[0]
            else:
                break
        answer.append(count)
    return answer




# progresses = [93, 30, 55]
# speeds = 	[1, 30, 5]
progresses = [95, 90, 99, 99, 80, 99]
speeds =    [1, 1, 1, 1, 1, 1]
a = solution(progresses, speeds)
print(a)