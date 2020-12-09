n = int(input())

list = list(map(int, input().split()))

count = 0

while True:
    if not all(item%2==0 for item in list):
        break

    list = [item/2 for item in list]
    count+=1

print(count)
