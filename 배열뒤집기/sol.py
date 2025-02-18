def solution(num_list):
    
    num_list.reverse() # reverse() 메소드는 원본을 바꾸고 출력은 하지않음, 출력하게되면 none 출력
    
    return num_list


print(solution([1, 2, 3, 4, 5])) # => [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) # => [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) # => [5, 3, 1, 1, 1, 0, 1]