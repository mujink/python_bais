from itertools import combinations
from collections import Counter, defaultdict
def solution(orders, course):
    answer = []
    lst = []
    num = []
    dic = defaultdict(int)
    for i in course:
        for menu in orders:
            if len(menu)>=i :
                lst += (list("".join(sorted(i)) for i in combinations(menu, i)))
    num = Counter(lst)
    lst = defaultdict(int)
    for j in num.items():
        for i in course:
            if (len(j[0]) == i) and (j[1] > dic[i]) :
                dic[i] = j[1]
    for j in num.items():
        answer += [j[0] for i in dic.items() if len(j[0]) == i[0] and i[1] == j[1] and i[1] >= 2]
    return sorted(answer)

# import collections
# import itertools

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)

#         most_ordered = collections.Counter(order_combinations).most_common()
#         print("most",most_ordered)
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
#         print("result",result)

#     return [ ''.join(v) for v in sorted(result) ]


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]
a = solution(orders, course)
print(a)