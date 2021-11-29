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
        #힙이 차있을때는 작은것을 팝
        else:
            print(heapq.heappop(heap))
    #힙에 푸시
    else:
        heapq.heappush(heap, x)