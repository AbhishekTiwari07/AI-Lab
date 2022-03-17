initial_state = ["R","R","R","_","C","C","C"]
final_state = ["C","C","C","_","R","R","R"]
state = initial_state
que = []

global_count = 0

def jump(i, j):
    state[i], state[j] = state[j], state[i]
    return state

def print_state(state):
    for x in state:
        print(x, end=' ')

def upcount():
    global global_count
    global_count += 1

def dfs():
    flag = 0

    global global_count
    global_count += 1

    if state == final_state:
        print('Final State Reached: ', state)
        
    for i in range(7):
        if state[i] == 'R':
            if i + 1 < 7 and state[i + 1] == '_':
                state[i] = '_'
                state[i + 1] = 'R'
                flag = 1
                dfs()
                state[i] = 'R'
                state[i + 1] = '_'
            if i + 2 < 7 and state[i + 2] == '_':
                state[i] = '_'
                state[i + 2] = 'R'
                flag = 1
                dfs()
                state[i] = 'R'
                state[i + 2] = '_'

        elif state[i] == 'C' :
            if i - 1 >= 0 and state[i - 1] == '_':
                state[i] = '_'
                state[i - 1] = 'C'
                flag = 1
                dfs()
                state[i] = 'C'
                state[i - 1] = '_'
            if i - 2 >= 0 and state[i - 2] == '_':
                state[i] = '_'
                state[i - 2] = 'C'
                flag = 1
                dfs()
                state[i] = 'C'
                state[i - 2] = '_'

    # if flag == 0:
    #     print(state) 


def bfs(state):
    que.append(state)

    visited = []
    count = 0

    while que:
        state = que.pop(0)
        count += 1

        if state == final_state:
            print('Final State Reached: ', state)
            return count

        if state in visited:
            continue

        visited.append(state)

        for i in range(7):
            if state[i] == 'R':
                if i + 1 < 7 and state[i + 1] == '_':
                    new_state = state[:]
                    new_state[i] = '_'
                    new_state[i + 1] = 'R'
                    que.append(new_state)

                if i + 2 < 7 and state[i + 2] == '_':
                    new_state = state[:]
                    new_state[i] = '_'
                    new_state[i + 2] = 'R'
                    que.append(new_state)

            elif state[i] == 'C' :
                if i - 1 >= 0 and state[i - 1] == '_':
                    new_state = state[:]
                    new_state[i] = '_'
                    new_state[i - 1] = 'C'
                    que.append(new_state)

                if i - 2 >= 0 and state[i - 2] == '_':
                    new_state = state[:]
                    new_state[i] = '_'
                    new_state[i - 2] = 'C'
                    que.append(new_state)
    return count

dfs()
print('Solved using DFS after exploring ', global_count, ' Nodes')

print('Solved using DFS after exploring ', bfs(state), ' Nodes')