n = input()
#크로아티아 알파벳
arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
#n에서 배열안에 있는 알파벳을 찾으면 a로 바꿔줌
for i in arr:
    n = n.replace(i, 'a')
print(len(n))