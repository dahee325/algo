def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in vowels:
        my_string = my_string.replace(i, '')
    return my_string

print(solution('bus')) # => 'bs'
print(solution('nice to meet you')) # => 'nc t mt y'