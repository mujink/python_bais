# def solution(priorities, location):
#     A = [x for x in range(len(priorities))]
#     B = []
#     count = 0
#     # for i in range(len(priorities)-1):
#     while len(priorities) != 0:
#         b = max(priorities)
#         while priorities[0] != b:
#             time = priorities[0]
#             del priorities[0]
#             lst = priorities
#             for j in range(len(lst)):
#                 count += 1
#                 if time < lst[j]:
#                     lst.append(time)
#                     A.append(A[0])
#                     del A[0]
#                     break
#         B.append([lst[0], A[0]])
#         del lst[0]
#         del A[0]
#     for i, x in enumerate(B):
#         if x[1] == location:
#             return i+1

def solution(priorities, location):
    A = [i for i in range(len(priorities))]
    B = priorities.copy()
    i = 0
    while True:
        if B[i] < max(B[i+1:]):
            A.append(A.pop(i))
            B.append(B.pop(i))
        else:
            i += 1
        if B == sorted(B, reverse=True):
            break
    return A.index(location)+1

# priorities = [2, 1, 3, 2]
# location =    2
priorities = [1, 2, 3, 2]
location =    1
# priorities = [1, 1, 9, 1, 1, 1]
# location =    0
# p = np.array(priorities)
# p = 100 - p
# print(len(p))
# print(p)
a = solution(priorities, location)
print(a)