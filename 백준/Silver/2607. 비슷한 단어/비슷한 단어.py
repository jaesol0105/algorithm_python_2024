from collections import defaultdict

N = int(input())
first_word = list(input())
first_word_cnt = defaultdict(int)
for c in first_word:
    first_word_cnt[c] += 1

result = 0
for _ in range(N-1):
    word = list(input())
    if abs(len(word)-len(first_word)) <= 1:
        word_cnt = defaultdict(int)
        for c in word:
            word_cnt[c] += 1
        flag = 0
        for x in range(ord('A'), ord('Z')+1):
            if first_word_cnt[chr(x)] != word_cnt[chr(x)]:
                flag += abs(first_word_cnt[chr(x)] - word_cnt[chr(x)])

        if flag <= 2:
            result += 1

print(result)