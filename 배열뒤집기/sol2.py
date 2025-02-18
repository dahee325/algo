def solution(num_list):
    result = []
    for num in num_list:
        result.insert(0, num) # 새로운 숫자가 들어올 때마다 0번째에 들어오기때문에 처음에 넣은 숫자가 하나씩 뒤로 밀려나게된다.

    return result


print(solution([1, 2, 3, 4, 5])) # => [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) # => [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) # => [5, 3, 1, 1, 1, 0, 1]