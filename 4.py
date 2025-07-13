'''
8 5
1 3 5 7 9 11 13 15
2
4
6
8
20
'''
N, M = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(M):
    B = int(input())
    for i in range(N):
        if B <= arr[i]:
            print(len(arr) - i)
            break
    else:
        print(0)