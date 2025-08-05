T = int(input())


for test_case in range(1, T+1):

    ##########################
    N = int(input())
    lst = list(map(int, input()))
    count = [0] * 10 # 횟수
    # numbers = [0] * 10 # 실제 값
    # print(lst)


    for i in range(N): # 횟수
        count[lst[i]] += 1


    max_count = max(count) # 최대 장수 뽑기

    #떴을 때 for문을 멈춘다. (특정 조건에서만 발동시키고 멈추려면 for / break)
    for i in range(9, -1, -1):
        if count[i] == max_count:
            print(f'#{test_case} {i} {count[i]}')
            break
    
    ############################


    # print(count)


    # for j in range(1, 10): # count의 누적합
    #     count[j] += count[j-1]

    # print(count)
    

    # for k in range(len(lst)-1, -1, -1): # len(lst)-1은 들어온 최초의 리스트의 길이-1(왜 빼기 1을 하냐면 인덱스 번호가 1 적게부터 시작하기 때문에) 을말하고 stop은 원소의 최솟값 0
    #     count[lst[k]] -= 1
    #     numbers[count[lst[k]]] = lst[k]

    # print(numbers)
    ###########################

    






#     N = int(input())
#     lst = list(map(int, input()))
#     count = [0] * 10 # 횟수
#     numbers = [0] * 10 # 실제 값

#     for i in range(N):
#         count[lst[i]] += 1
#         numbers[lst[i]] += lst[i]
    
#     print(count)
#     print(numbers)

#     result_nubmer = max(numbers)
#     result_count = max(count)

#    print(f'#{test_case} {int(result_nubmer/result_count)} {result_count}')
