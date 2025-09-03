# 비트 연산은 어떻게 활용할까?
# 게임에서 사용
# 조건문보다 하이 레벨
# 비트 연산은 상태를 관리할 때 많이 사용된다.
WALK = 1 << 0
ATTACK = 1 << 1
JUMP = 1 << 2

character_state = 0

def set_state(state, flag):
    return state | flag

def unset_state(state, flag):
    return state & ~flag

character_state = set_state(character_state, WALK)
character_state = unset_state(character_state, WALK)
