while True:
    num = input()
    if num == '0':
        break
    #문자열을 뒤집어서 원래것과 같으면 yes출력       
    if num == num[::-1]:
        print('yes')
    else:
        print('no')