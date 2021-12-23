while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    #첫번째수가 두번째수로 나눠 떨어질경우 배수
    if n%m==0:
        print('multiple')
    #두번쨰수가 첫번째수로 나눠 떨어질경우 약수
    elif m%n==0:
        print('factor')
    else:
        print('neither')