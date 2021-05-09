from collections import Counter
from functools import reduce
def solution(clothes):
    d = Counter([b for a, b in clothes])
    answer = reduce(lambda x,y: x*(y+1), d.values(),1) -1
    return answer



clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
a = solution(clothes)
print(a)