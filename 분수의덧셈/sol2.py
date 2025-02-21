def solution(numer1, denom1, numer2, denom2):
    answer = []
    if denom1 == denom2:
        num = numer1 + numer2
        den = denom1 + denom2
        for i in range(1, num+1)
            if num % i == 0 and den % i == 0:
                num = num // i
                den = den // i
                return [num, den]
            else:
                return [num, den]
    else:
        for j in range(1, denom1+1)
            if 
    return answer


print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))