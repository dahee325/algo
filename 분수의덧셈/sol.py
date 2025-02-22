from math import gcd

def solution(numer1, denom1, numer2, denom2):
    # math.gcd() # 최대공약수
    num = numer1 * denom2 + numer2 * denom1
    den = denom1 * denom2
    
    number = gcd(num, den)
    num //= number
    den //= number
    return [num, den]


print(solution(1, 2, 3, 4)) # => [5, 4]
print(solution(9, 2, 1, 3)) # => [29, 6]]

# def solution(numer1, denom1, numer2, denom2):
#     # math.gcd() # 최대공약수
#     answer = []
    
    # if denom1 == denom2:
    #     num = numer1 + numer2
    #     den = denom1
    #     for i in range(1, num+1):
    #         if num % i == 0 and den % i == 0:
    #             num = num // i
    #             den = den // i
    #             answer.append(num)
    #             answer.append(den)
    #         else:
    #             answer.append(num)
    #             answer.append(den)    
    # else:
    #     num = numer1 * denom2 + numer2 * denom1
    #     den = denom1 * denom2
    #     for i in range(1, num+1):
    #         if num % i == 0 and den % i == 0:
    #             num = num // i
    #             den = den // i
    #             answer.append(num)
    #             answer.append(den)            
    #         else:
    #             answer.append(num)
    #             answer.append(den)
    # return answer