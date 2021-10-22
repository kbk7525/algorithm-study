n = int(input())
word = []
for i in range(n):
    word.append(input())
new_word = set(word) #겹치는 경우 뺴고 저장
word = list(new_word) #word에 다시 저장
word.sort() #사전순으로
word.sort(key=len) #길이 순서대로
for i in word:
    print(i)