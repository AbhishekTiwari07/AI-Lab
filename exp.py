# state ------ ####
# (M,C) _____ (M,C)
# (0,0) _____ (3,3)
# (1,1) _____ (2,2)
# [[1,1],     [2,2]]
# (3,3) _____ (0,0) 

initial_state = [[0, 0], [3, 3]]

final_state = [[3, 3], [0, 0]]

visited = dict()

def isValid(state):
    if state[0][0] < 0 or state[0][1] < 0 or state[1][0] < 0 or state[1][1] < 0:
        return False
    elif state[0][0] == 0 :
        return state[1][0] >= state[1][1]
    elif state[1][0] == 0 :
        return state[0][0] >= state[0][1]
    return state[1][0] >= state[1][1] and state[0][0] >= state[0][1]

def dfs(state):
    print(visited)
    if state == final_state:
        print("GG")
        return
        
    if state in visited:
        return

    # if not isValid(state):
    #     return 
    
    new_state = state[:]
    visited[new_state] = True

    # 1M L-R
    new_state = state[:]
    new_state[0][0] += 1
    new_state[1][0] -= 1
    dfs(new_state)

    # 1M R-L
    new_state = state[:]
    new_state[0][0] -= 1
    new_state[1][0] += 1
    dfs(new_state)

    # 1C L-R
    new_state = state[:]
    new_state[0][1] += 1
    new_state[1][1] -= 1
    dfs(new_state)

    # 1C R-L
    new_state = state[:]
    new_state[0][1] -= 1
    new_state[1][1] += 1
    dfs(new_state)

    # 1C 1M L-R
    new_state = state[:]
    new_state[0][1] += 1
    new_state[1][1] -= 1
    new_state[0][0] += 1
    new_state[1][0] -= 1
    dfs(new_state)

    # 1C 1M R-L
    new_state = state[:]
    new_state[0][1] -= 1
    new_state[1][1] += 1
    new_state[0][0] -= 1
    new_state[1][0] += 1
    dfs(new_state)

    new_state = state[:]
    new_state[0][0] += 2
    new_state[1][0] -= 2
    dfs(new_state)

    new_state = state[:]
    new_state[0][0] -= 2
    new_state[1][0] += 2
    dfs(new_state)

    new_state = state[:]
    new_state[0][1] += 2
    new_state[1][1] -= 2
    dfs(new_state)

    new_state = state[:]
    new_state[0][1] -= 2
    new_state[1][1] += 2
    dfs(new_state)


dfs(initial_state)
# visited.append(initial_state)
# visited.append(initial_state)