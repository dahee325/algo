def solution(num_list):
    return num_list[::-1] # [시작점:끝나는점:얼만큼자를건지], -1을 넣으면 뒤에서부터 자른다(역순과 동일한 효과)


print(solution([1, 2, 3, 4, 5])) # => [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) # => [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) # => [5, 3, 1, 1, 1, 0, 1]