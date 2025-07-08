'''
이 문제는 선입선출, 전형적인 큐 문제이다.
1번 케이스 일 때 큐 리스트를 만들어 차례대로 삽입한다.
2번 케이스일 경우 맨 앞의 학생이 빠진다.
이때 큐의 길이와 맨 마지막 학생의 정보를 기록한다.
반복이 끝났을 때 큐의 길이가 가장 길었을 때의 길이와 마지막 학생의 번호를 출력한다.
'''

N = int(input())
queue = []
record = []
for n in range(N):
    info = input().split()
    if len(info) == 2:
        case, p_number = int(info[0]), int(info[1])
        queue.append(p_number)
        record.append((len(queue), queue[-1]))
    else:
        case, p_number = int(info[0]), None
        queue.pop(0)
        record.append((len(queue), queue[-1]))
record.sort(reverse=True)
record_max_len = []
for i in range(N):
    if record[i][0] == record[i + 1][0]:
        record_max_len.append(record[i])
        record_max_len.append(record[i + 1])
    else:
        break
record_max_len.sort()
print(record_max_len[0][0], record_max_len[0][1])


