n = int(input())
person = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    person.append((age, name))
person.sort(key=lambda i: i[0]) #람다식을 이용해 나이순으로 정렬
for i in person:
    print(i[0], i[1])