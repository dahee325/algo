# 잘못된 풀이래요...

def solution(bin1, bin2):
    answer = ''
    for i in range(0, len(bin1)):
        if bin1[i] == '0' and bin2[i] == '0':
            answer += '0'
        elif bin1[i] == '0' or bin2[i] == '0':
            answer += '1'
        else:
            answer += '10'
    return ''.join(answer)


print(solution('10', '11'))
print(solution('1001', '1111'))