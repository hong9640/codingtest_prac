'''
5 4
kor kor eng eng math
kor
eng
math
-
'''
N, M = map(int, input().split())
subject = input().split()
sub_count = {}
# get 메서드를 이용해 딕셔너리에 갯수 쓰기
for sub in subject:
    sub_count[sub] = sub_count.get(sub, 0) + 1
for _ in range(M):
    sub_input = input()
    if sub_input in sub_count:
        print(sub_count[sub_input])
    else:
        print(len(subject))

