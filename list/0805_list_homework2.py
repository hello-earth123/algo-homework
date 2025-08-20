# N은 정류장 번호(인덱스 번호) 총 정류장 갯수는 N+1개 / K는 한 번 충전으로 이동할 수 있는 정류장 수
# 충전기가 설치된 정류장 번호가 M으로 주어진다

# 가능하면 충전 횟수 출력 / 불가능하면 0 출력
T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split()) 

    charger = list(map(int, input().split()))
    bus_stop = [0] * (N+1)

    position = 0 # 버스의 현위치
    result = 0 # 충전해야하는 총 횟수
    #######################
    
    
    # 충전기가 있는 bus_stop list 만들기 / 충전기 있으면 1, 없으면 0
    for i in range(M):
        bus_stop[charger[i]] += 1

    # print(bus_stop)


    while position + K < N: # 버스가 현위치에서 최대로 이동하여도 제일 끝 정류장보다는 작을 때 까지만 반복
        for step in range(K, 0, -1):
            if bus_stop[position + step] == 1:
                position += step
                result += 1
                break
            
        else:
            result = 0
            break

    #########################

    print(f'#{test_case} {result}')