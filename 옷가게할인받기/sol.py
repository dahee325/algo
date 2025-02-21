def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price


print(solution(150000)) # => 142500
print(solution(580000)) # => 464000