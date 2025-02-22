def solution(array):
    dic = {}
    v = []

    for num in array:
        if num in dic.keys():
            dic[num] += 1
        else:  
            dic[num] = 1
    
    max_num = max(dic.values())
    for key, value in dic.items():
        if value == max_num:
            v.append(key)

    if len(v) == 1:
        return v[0]
    else:
        return -1

print(solution([1, 2, 3, 3, 3, 4])) # => 3
print(solution([1, 1, 2, 2])) # => -1
print(solution([1])) # => 1