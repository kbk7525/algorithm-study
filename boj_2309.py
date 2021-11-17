import sys
height = []
for _ in range(9):
    height.append(int(sys.stdin.readline()))
s = sum(height)
#완전탐색을 하면서 전체합에서 두개의 원소를 빼면 100이 되는값을 찾아 n1, n2에 저장
for i in range(9):
    for j in range(i+1, 9):
        if s-(height[i]+height[j])==100:
            n1=height[i]
            n2=height[j]
#n1, n2 제거
height.remove(n1)
height.remove(n2)
height.sort() #오름차순 정렬
for i in height:
    print(i)