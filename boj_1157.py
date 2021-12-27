word = input().lower() #입력받은것을 소문자로 변환
new_word = list(set(word)) #겹치는 알파벳을 제거
freq = [] #알파벳 빈도수를 저장하는 리스트
#입력받은것중 i랑 같은것을 카운트해줌
for i in new_word:
    freq.append(word.count(i))
#최대값이 1개가 넘을경우
if freq.count(max(freq)) > 1:
    print('?')
#최대빈도수를 가진 알파벳의 인덱스를 찾아 대문자로 변환해서 출력
else:
    print(new_word[freq.index(max(freq))].upper())