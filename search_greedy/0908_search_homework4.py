# 0 ~ 9까지
# 연속인 숫자가 3개 이상이면 run
# 같은 숫자가 3개 이상이면 triplet
# 교대로 한 장 씩 
# 6장 전에 run이나 triplet 나오면 끝

# 리스트 순서대로 가져간다.
# 1번이 승자면 1, 2번이 승자면2, 무승부이면 0
T = int(input())

for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    count_triplet1 = 1
    count_run1 = 1
    count_triplet2 = 1
    count_run2 = 1
    is_winner = False
    for idx in range(len(cards)):
        if idx % 2 == 0:
            player1.append(cards[idx])
            player1.sort()
            num1 = -100
            for i in range(len(player1)):
                # run인 경우
                if player1[i] == num1:
                    count_run1 += 1
                    num1 = player1[i]
                elif player1[i] == num1 + 1:
                    count_triplet1 += 1
                    num1 = player1[i]  
                else:
                    count_run1 = 1
                    count_triplet1 = 1
                    num1 = player1[i]

                if count_run1 >= 3 or count_triplet1 >= 3:
                    result = 1
                    is_winner = True
            if is_winner:
                break        

        else:
            player2.append(cards[idx])
            player2.sort()
            num2 = -100
            for i in range(len(player2)):
                # run인 경우
                if player2[i] == num2:
                    count_run2 += 1
                    num2 = player2[i]
                elif player2[i] == num2 + 1:
                    count_triplet2 += 1
                    num2 = player2[i]
                else:
                    count_run2 = 1
                    count_triplet2 = 1
                    num2 = player2[i]
    
                if count_run2 >= 3 or count_triplet2 >= 3:
                    result = 2
                    is_winner = True
            if is_winner:
                break 

    if not is_winner:
        result = 0
    print(f'#{test_case} {result}')