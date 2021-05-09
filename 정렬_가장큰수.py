# def solution(numbers):
#     from functools import cmp_to_key
#     numbers = list(map(str, numbers))
#     numbers = sorted(numbers, key=cmp_to_key(lambda x, y:int(x+y) - int(y+x)), reverse=True)
#     answer = ''.join(numbers)
#     return answer if answer[0] != "0" else "0"

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    # numbers.sort(key=lambda x: x*3)
    return str(int(''.join(numbers)))

test = [3, 30, 34, 5, 9]
	# "9534330"
returns = solution(test)
print(returns)