# def solution(citations):
#     a = []
#     citations.sort(reverse=True)
#     print(citations)
#     for index, value in enumerate(citations, start=1):
#         if index > value:
#             a = index-1
#             break
#     answer = a
#     return answer

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

citations = [3, 0, 6, 1, 5]
returns = solution(citations)
print(returns)