def solution(array, commands):
    answer = []
    for value in commands:
        i = value[0]-1
        j = value[1]
        k = value[2]-1
        arrays = array[i:j]
        arrays.sort()
        answer += arrays[k:k+1]
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
returns = solution(array,commands)
print(returns)