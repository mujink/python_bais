# def solution(new_id):
#     step1 = True
#     step2 = True
#     step3 = True
#     step4 = True
#     step5 = True
#     step6 = True
#     step7 = True
        
#     if step1 :
#         new_id = new_id.lower()
#     if step2 :
#         id = ""
#         for c in new_id:
#             if c.isalnum():
#                 id += c
#             if c == "_" or c == "-" or c==".":
#                 id += c
#             print(id)
            
#     if step3 :
#         id2 = ""
#         for index in range(len(id)):
#             if index+1 == len(id):
#                 id2 += id[index]
#                 continue
#             if (id[index]==".")and(id[index] == id[index+1]):
#                 continue
#             id2 += id[index]
#     if step4 :
#         id = list(id2)
#         one_leng = (len(id)==1)
#         if one_leng :
#             if id[0]==".":
#                 del id[0]  
#         if not one_leng:
#             first = (id[0]==".")
#             end = (id[-1]==".")
#             if first:
#                 del id[0]
#             if end:
#                 del id[-1]
#         id = "".join(x for x in id)
            
#     if step5 :
#         if len(id) == 0:
#             id += ("a")
#     if step6 :
#         id = list(id)
#         if len(id) >= 16:
#             id =  id[:15]
#         if id[-1] == ".":
#             del id[-1]
#         id = "".join(x for x in id)
#     if step7 :
#         while len(id) <= 2:
#             id += (id[-1])
#     answer = id
#     return answer

import re

def solution(new_id):
    level4 = re.sub("^\.|\.$","",re.sub("\.+",".",re.sub("[^a-z0-9-_\.]","",new_id.lower())))
    if len(level4) == 0: level4 += "a"
    if len(level4) >= 16: 
        level4 = level4[:15]
        if level4[14] == ".": level4 = level4[:14]
    if len(level4) <= 2: level4 = level4.ljust(3,level4[-1]) 

    return level4
    
test1 = "...!@BaT#*..y.abcdefghijklm"
test2 = "z-+.^."
test3 = "=.="
test4 = "123_.def"
test5 = "abcdefghijklmn.p"
print(solution(test1))