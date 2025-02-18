def solution(my_string):
    answer = 0
    numbers = []

    for char in my_string:
        if char.isdigit(): # isdigit() : 문자를 숫자로 반환할 수 있나요?있으면 반환
            numbers.append(int(char))
        
    return sum(numbers)


print(solution('aAb1B2cC34oOp')) # => 10
print(solution('1a2b3c4d123')) # => 16