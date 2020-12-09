N = int(input())
list = list(map(int, input().split()))

Alice = 0
Bob = 0

for count in range(N):
    max_value = max(list)

    if count%2 == 0:
        Alice += max_value
    else:
        Bob += max_value

    list.remove(max_value)

print(Alice - Bob)