def solution(array, n):
    array.sort()
    temp = []
    for i in array:
        temp.append(abs(n-i))
    return array[temp.index(min(temp))]


print(solution([3, 1, 28], 20)) # => 28
print(solution([10, 11, 12], 13)) # => 12