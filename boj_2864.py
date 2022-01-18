#replace를 이용하면 되는 간단한문제
a,b=map(str, input().split())
min_v=int(a.replace('6','5'))+int(b.replace('6','5')) #6이 있으면 전부 5로 바꿔줌
max_v=int(a.replace('5','6'))+int(b.replace('5','6')) #5가 있으면 전부 6으로 바꿔줌
print(min_v, max_v)