# import pandas as pd
# from itertools import chain, combinations
# def key_options(items):
#     return chain.from_iterable(combinations(items, r) for r in range(1, len(items)+1) )

# def solution(relation):
#     Candidate = []
#     df = pd.DataFrame(data = relation)
#     for candidate in key_options(list(df)):
#         deduped = df.drop_duplicates(candidate)
#         if len(deduped.index) == len(df.index):
#             Candidate.append(set(candidate))
#     k = 0
#     while k <len(Candidate) :

#         for i in Candidate[k+1:] :

#             if Candidate[k].issubset(i) :
#                 Candidate.remove(i)
#         k += 1
#     return len(Candidate)


def solution(relation):
    answer_list = list()

    for i in range(1, 1 << len(relation[0])): #0~15
        tmp_set = set()
        for j in range(len(relation)): #0~5
            tmp = ''
            for k in range(len(relation[0])): #0~3
                if i & (1 << k):                #0~15, 1~8 (1: 학번, 2: 이름, 4: 학과, 8: 학년)
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)
        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)


relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]
a = solution(relation)
print(a)