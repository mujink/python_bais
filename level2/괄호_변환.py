# def abcd (u):
#     a = 0
#     u = list(u)
#     for i in range(len(u)):
#         if u[0] == ")":
#             return False
#         elif u[i] == "(":
#             a += 1
#         elif u[i] == ")":
#             a -= 1
#     if a == 0:
#         return True

# def solution(p):
#     dic = {"(": 0,")": 0}
#     u = ""
#     ret = ""
#     for i in p:
#         u += i
#         if i == "(":
#             dic["("] +=1
#         elif i == ")":
#             dic[")"] +=1
#         if dic["("] == dic[")"]:
#             break
#     if u != "":
#         if abcd(u):
#             un = solution(p[len(u):])
#             u += un
#             return u
#         else:
#             ret += "("
#             un = solution(p[len(u):])
#             ret += un
#             ret += ")"
#             u = u[1:-1]
#             lst = ""
#             for i in range(len(u)):
#                 if u[i] == "(":
#                     lst += ")"
#                     continue
#                 lst += "("
#             ret += lst
#             return ret
#     return u

def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))


p = "(()())()"
# p = ")("
# p = "()))((()"
a = solution(p)
print(a)