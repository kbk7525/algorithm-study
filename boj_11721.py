s = input()
print(s[0], end='')
for i in range(1, len(s)):
    if i%10==0:
        print()
    print(s[i], end='')