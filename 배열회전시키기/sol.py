def solution(numbers, direction):
    answer = []
    if direction == 'right':
        return ([numbers[-1]] + numbers[:-1])
    elif direction == 'left':
        return (numbers[1:] + [numbers[0]])


print(solution([1, 2, 3], 'right')) # => [3, 1, 2]
print(solution([4, 455, 6, 4, -1, 45, 6], 'left')) # => [455, 6, 4, -1, 45, 6, 4]