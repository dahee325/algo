# 버블정렬 : 앞에서부터 2개씩 비교하면서 큰 수를 뒤로 보냄
def solution(numbers):
    n = len(numbers)
    
    # .sort()
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers[-1] * numbers[-2]


print(solution([1, 2, 3, 4, 5])) # => 20
print(solution([0, 31, 24, 10, 1, 9])) # => 744