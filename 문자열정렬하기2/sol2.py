def solution(my_string):
    answer = []

    for string in my_string:
        if ord('A') <= ord(string) <= ord('Z'):
            answer.append(chr(ord(string)+32)) # 소문자로 바꾸기위해 32를 더함함
        else:
            answer.append(string)
    return ''.join(answer)    

print(solution('Bcad')) # => 'abcd'
print(solution('heLLo')) # => 'ehllo'
print(solution('Python')) # => 'hnopty'