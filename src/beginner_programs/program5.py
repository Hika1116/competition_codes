N, A, B = map(int, input().split())

ans = 0

for num in range(N+1):
    sum_num = sum(map(int, str(num)))
    if A<=sum_num<=B:
        ans+=num


print(ans)