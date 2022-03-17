# state ------ ####
# (M,C) _____ (M,C)
# (0,0) _____ (3,3)
# (1,1) _____ (2,2)
# [[1,1],     [2,2]]
# (3,3) _____ (0,0) 

initial_state = [[0, 0], [3, 3]]

final_state = [[3, 3], [0, 0]]

visited = []

current_state = initial_state

def isValid(state):
    if state[0][0] == 0 :
        return state[1][0] >= state[1][1]
    elif state[1][0] == 0 :
        return state[0][0] >= state[0][1]

    return state[1][0] >= state[1][1] and state[0][0] >= state[0][1]

def dfs(state):
    print(state, isValid(state), visited)

    if state == final_state:
        print("GG")
        return
        
    if state in visited:
        return

    if not isValid(state):
        return 
    
    visited.append(state)

    state[0][0] += 1
    state[1][0] -= 1
    dfs(state)
    state[0][0] -= 1
    state[1][0] += 1
    
    state[0][1] += 1
    state[1][1] -= 1
    dfs(state)
    state[0][1] -= 1
    state[1][1] += 1


def 

dfs(initial_state)