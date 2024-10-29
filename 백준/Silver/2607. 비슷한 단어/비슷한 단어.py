N = int(input())
first_word = input()
result = 0

for _ in range(N - 1):
    word = input()
    cnt = 0
    for c in first_word:
        if c in word:
            word = word.replace(c,'',1)
        else:
            cnt += 1 # fist_word의 남은 글자
    if len(word) < 2 and cnt < 2: # word의 남은 글자
        result += 1
        
print(result)