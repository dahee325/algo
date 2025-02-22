def solution(rsp):
    answer = ''
    dic = {
        '0': '5', 
        '2': '0',
        '5': '2',
    }
    for i in rsp:
        answer += dic[i]
    return ''.join(answer)
    # return ''.join(d[i] for i in rsp)


print(solution('2')) # => 0
print(solution('205')) # => 052