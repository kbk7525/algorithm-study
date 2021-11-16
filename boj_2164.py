from collections import deque
queue = deque()
n = int(input())
#1부터 n까지 queue에 푸시
for i in range(1,n+1):
    queue.append(i)
num = queue[0] #마지막에 남는수 초기화
#queue에 들어있는 원소가 있을때까지 반복
while len(queue) > 1:
    queue.popleft() #맨위의 카드는 버림
    queue.append(queue.popleft()) #그다음 제일 위에 있는 카드를 queue의 밑으로 옮김
    num = queue[-1] #queue의 맨마지막 원소를 num에 저장
print(num)