def solution(price):
    discount = {
        500000: 0.8,
        300000: 0.9,
        100000: 0.95,
        0: 1,
    }
    for p, r in discount.items():
        if price >= p:
            return int(price * r)
            
print(solution(150000)) # => 142500
print(solution(580000)) # => 464000