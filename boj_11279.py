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
        #힙이 차있을때는 -1을 곱해서 큰 것을 팝
        else:
            print(-1*heapq.heappop(heap))
    #힙에 푸시 (-를 붙인이유는 큰수가 음수가 되면 가장작아지기 떄문)
    else:
        heapq.heappush(heap, -x)