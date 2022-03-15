import numpy as np
import matplotlib.pyplot as plt


class Place:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def euclidean_distance(a, b):
    return np.sqrt(((a.x - b.x) ** 2 + (a.y - b.y) ** 2))

def tot_euc_dist(location):
    dist = 0
    for i, j in zip(location[1:],location[:-1]):
        dist += euclidean_distance(i, j)
    dist += euclidean_distance(location[0], location[-1])
    return dist

x = np.random.uniform(0, 100, size=25)
y = np.random.uniform(0, 100, size=25)

location = []

for i,j in zip(x, y):
    location.append(Place(i,j))

fig = plt.figure(figsize=(30, 12))
axes1 = fig.add_subplot(121)
axes2 = fig.add_subplot(122)

purana_cost = tot_euc_dist(location)

axes1.scatter(x, y)

for f, s in zip(location[:-1], location[1:]):
    axes1.plot([f.x, s.x], [f.y, s.y], "b")
    axes1.plot([location[0].x, location[-1].x], [location[0].y, location[-1].y], "b")

epochs = 200
T = 30
factor = 0.995

for i in range(epochs):
    for j in range(100):
        a, b = np.random.randint(0, len(location), size=2)

        location[a],location[b] = location[b],location[a]

        naya_cost = tot_euc_dist(location)
        
        if naya_cost > purana_cost:
            val = np.random.uniform()
            print((purana_cost - naya_cost))
            if val < (1 / (1 + np.exp((purana_cost - naya_cost) * (-1) / T))):
                purana_cost = naya_cost
            else:
                location[a], location[b] = location[b], location[a]
        else: 
            purana_cost = naya_cost

    T = T*factor

axes2.scatter(x, y)
for f, s in zip(location[:-1], location[1:]):
    axes2.plot([f.x, s.x], [f.y, s.y], "r")
    axes2.plot([location[0].x, location[-1].x], [location[0].y, location[-1].y], "r")

plt.show()