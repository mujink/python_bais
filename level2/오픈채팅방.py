def solution(record):
    answer = []
    log = dict()
    lst = dict()
    state = {0:"Enter", 1:"Leave", 2:"Change"}
    for num, i in enumerate(record):
        i = i.split(" ")
        if i[0] == state[0]:
            lst[i[1]] = i[2]
            log[num] = i[1],"님이 들어왔습니다."            
        elif i[0] == state[1]:
            log[num] = i[1],"님이 나갔습니다."
        elif i[0] == state[2]:
            lst[i[1]] = i[2]
    for index in range(len(log)):
        answer.append(lst[log[index][0]]+log[index][1])
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

a = solution(record)
print(a)