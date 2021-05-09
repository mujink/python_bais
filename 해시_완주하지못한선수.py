# def solution(s,c):
#     s.sort()
#     c.sort()
#     for par, com in zip(s, c) :
#         if par != com :
#             return par   # 예시 1번
#     return s[-1]         # 예시 2번

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
a = collections.Counter(participant)
b = collections.Counter(completion)
print(a)
print(b)
print(a-b)
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
result = solution(participant, completion)
print(result)