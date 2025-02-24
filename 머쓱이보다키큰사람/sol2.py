def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height) # height의 인덱스번호 출력
    
    
print(solution([149, 180, 192, 170], 167)) # => 3
print(solution([180, 120, 140], 190)) # => 0