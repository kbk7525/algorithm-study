n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    for i in range(len(word)):
        if i != len(word)-1: 
            #다음 글자와 같으면 continue
            if word[i] == word[i+1]:
                continue
            #지금 글자와 나머지글자중 포함되는게 있으면 break
            elif word[i] in word[i+1:]:
                break
        else:
            cnt += 1
print(cnt)