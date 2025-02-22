def solution(my_string, num1, num2):
    string = list(my_string)
    string[num1], string[num2] = string[num2], string[num1]
    return ''.join(string)


print(solution('hello', 1, 2)) # => 'hlelo'
print(solution('I love you', 3, 6)) # => 'I l veyou'