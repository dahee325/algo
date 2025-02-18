def solution(my_string):
    answer = 0
    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('z'))
        # 글자가 아닌가요? => 숫자인가요?
        # char가 아스키코드에서 'A'와 'z'사이에 있나요? => 문자인가요?
        # ord : 아스키코드에서의 문자(숫자, 알파벳 등)의 번호를 알려줌 
            answer += int(char)
    
    return answer


print(solution('aAb1B2cC34oOp')) # => 10
print(solution('1a2b3c4d123')) # => 16