'''
이 문제는 1번 문제와 비슷한 큐 문제이다.
한 변수에 각 유형의 정보를 담고 이의 길이를 확인한 후 유형에 맞게 이 값들을 각각의 변수에 할당한다.
큐 리스트를 생성한다. 여기에 학생 번호를 넣는다.
좋아하는 음식을 먹은 학생과 아닌 학생을 구분할 각 변수를 생성에 리스트를 할당한다.
그리고 2번 케이스가 나왔을 때 좋아하는 음식을 먹을 수 있는지 유무에 따라 각 리스트에 학생 번호를 넣는다.
반복이 끝난 후, 좋아하는 음식의 섭취 유무를 확인하는 리스트에서 아래와 같이 정보를 확인해 출력한다.
출력 시 좋아하는 음식을 먹은 학생의 목록을 빈칸이 있게 출력한다.
다음으로 좋아하는 음식을 먹지 못한 학생의 목록을 빈칸이 있게 출력한다.
마지막으로 아예 음식을 먹지 못한 학생을 빈칸이 있게 출력한다.
단, 학생 목록에 학생이 없는 경우 none을 출력한다.
6
1 2 1
1 1 1
2 1
1 3 2
2 2
2 2
'''

N = int(input())
queue = []
record = []
y_eat = []
n_eat = []
for _ in range(N):
    info = input().split()
    if len(info) == 3:
        case, p_num, menu_num = info
        queue.append((p_num, menu_num))
    if len(info) == 2:
        case, menu_num, p_num = info[0], info[1], None
        if menu_num == queue[0][1]:
            y_eat.append(queue[0][0])
            queue.pop(0)
        else:
            n_eat.append(queue[0][0])
            queue.pop(0)
y_eat.sort()
n_eat.sort()
print(*y_eat)
print(*n_eat)
if queue:
    print(*queue)
else:
    print(None)
