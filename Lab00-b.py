# (3,3,1) _____ (0,0,0)

Parent = dict()

class env:
    def __init__(self):
        self.initial_state = (3,3,0)
        self.final_state = (0,0,1)
        self.state = self.initial_state
        self.action = [[1,0], [0,1], [1,1], [2,0], [0,2]]

    def isValid(self, state):
        return (3 >= state[0] >= 0) and  (3 >=state[1] >= 0) and self.isMissionariesInMinority(state)

    def isMissionariesInMinority(self, state):
        return (state[0] == 0) or (3 - state[0] >= 3 - state[1] and state[0] >= state[1]) or state[0] == 3

    def dfs(self):
        stack = []
        count = 0
        stack.append(self.initial_state)
        while stack:
            count += 1
            cur_state = stack.pop()
            if self.final_state == cur_state:
                print("Solved using DFS")
                return count

            if tuple(cur_state) not in Parent:
                Parent[tuple(cur_state)] = []
            else:
                continue
            
            # Parent[A] = [B,C]
            # Parent[B] = [C]
            # Parent[C] = [else]
            # A -> B, C
            # B -> C
            # C -> else

            if cur_state[2] == 0:
                for i in self.action:
                    intermediate = (cur_state[0]- i[0], cur_state[1]- i[1], 1)
                    if not self.isValid(intermediate):
                        continue
                    Parent[tuple(cur_state)].append(intermediate)
                    if tuple(intermediate) not in stack and tuple(intermediate) not in Parent:
                        stack.append(intermediate)
            
            else:
                for i in self.action:
                    intermediate = (cur_state[0] + i[0], cur_state[1] + i[1], 0)
                    if not self.isValid(intermediate):
                        continue
                    Parent[tuple(cur_state)].append(intermediate)
                    if tuple(intermediate) not in stack and tuple(intermediate) not in Parent:
                        stack.append(intermediate)

        return count
    
    def bfs(self):
        queue = []
        queue.append(self.initial_state)
        count = 0
        while queue:
            cur_state = queue.pop(0)
            count += 1
            if self.final_state == cur_state:
                print("Solved using BFS")
                return count

            if tuple(cur_state) not in Parent:
                Parent[tuple(cur_state)] = []
            else:
                continue
            
            # Parent[A] = [B,C]
            # Parent[B] = [C]
            # Parent[C] = [else]
            # A -> B, C
            # B -> C
            # C -> else

            if cur_state[2] == 0:
                for i in self.action:
                    intermediate = (cur_state[0]- i[0], cur_state[1]- i[1], 1)
                    if not self.isValid(intermediate):
                        continue
                    Parent[tuple(cur_state)].append(intermediate)
                    if tuple(intermediate) not in queue and tuple(intermediate) not in Parent:
                        queue.append(intermediate)
            
            else:
                for i in self.action:
                    intermediate = (cur_state[0] + i[0], cur_state[1] + i[1], 0)
                    if not self.isValid(intermediate):
                        continue
                    Parent[tuple(cur_state)].append(intermediate)
                    if tuple(intermediate) not in queue and tuple(intermediate) not in Parent:
                        queue.append(intermediate)

        return count
        

conf = env()
print('Solved in : ', conf.bfs() - 1, 'steps')

Parent = {}
print('Solved in : ', conf.dfs() - 1, 'steps')

# cur_state = conf.final_state
# while cur_state != conf.initial_state:
#     for parent_i in Parent:
#         if cur_state in Parent[parent_i]:
#             print(parent_i)
#             cur_state = parent_i