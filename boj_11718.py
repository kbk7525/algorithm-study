#처음에는 무한반복만 해서 했는데 EOFError가 떴음
#그 다음에는 예외처리로 했는데 KeyboardInterrupt가 떴음
#KeyboardInterrupt도 예외처리해서 정답처리
while True:
    try:
        print(input())
    except KeyboardInterrupt:
        break
    except EOFError:
        break