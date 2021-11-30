import heapq #힙을 사용하기위한 라이브러리
import sys
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    #x가 0일 경우
    if x == 0:
        #힙이 빈경우
        if len(heap) == 0:
            print(0)
        #힙이 차있을때는 원래 수를 팝
        else:
            print(heapq.heappop(heap)[1])
    #힙에 푸시 (절댓값과 원래 수를 넣어서 절댓값을 기준으로 정렬함)
    else:
        heapq.heappush(heap, (abs(x), x))