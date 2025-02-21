def solution(my_string):
    answer = []
    vowels = 'aeiou'

    for i in my_string:
        if i not in vowels:
            answer.append(i)
    
    return ''.join(answer)
    # return "".join([i for i in my_string if not(i in "aeiou")])
            

print(solution('bus')) # => 'bs'
print(solution('nice to meet you')) # => 'nc t mt y')