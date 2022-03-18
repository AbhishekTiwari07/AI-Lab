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


# -------------------------------- Rajasthan Data ------------------------------------
# x = [76.12, 76.06, 76.62, 74.17, 75.27, 75.73,
#     73.53, 75.67, 72.94, 74.10, 76.48, 72.26,
#     76.96, 72.94,  75.12, 72.90,  72.62, 72.97,
#     72.81, 75.42 ]
# y = [26.62,25.65,27.26,26.61,23.57,25.30,
#     25.35,27.40,26.07,27.90,27.45,27.99,
#     27.84,24.83,24.28,23.03,27.88,27.11,
#     23.06, 24.15]


# -------------------------------- Random Points ------------------------------------
# x = np.random.uniform(0,100, size= 25)
# y = np.random.uniform(0,100, size= 25)


# -------------------------------- VLSI Data ------------------------------------
# file = "xqf131.tsp"

# file = "xqg237.tsp"

# file = "pma343.tsp"

# file = "pka379.tsp"

file = "bcl380.tsp"

infile = open(file, "r")
content = infile.readline().strip().split()

while content[0] != "NODE_COORD_SECTION":
    if content[0] == "DIMENSION":
        dimension = content[2]
    content = infile.readline().strip().split()
x = []
y = []

# Fill the x, y coordinates into the x, y
for i in range(0, int(dimension)):
    s, a, b = infile.readline().strip().split()[:]
    x.append(float(a))
    y.append(float(b))


location = []
costs = []

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

epochs = 5000
T = 50
factor = 0.995

for i in range(epochs):
    costs.append(purana_cost)
    for j in range(500):
        a, b = np.random.randint(0, len(location), size=2)

        location[a],location[b] = location[b],location[a]

        naya_cost = tot_euc_dist(location)
        
        if naya_cost > purana_cost:
            val = np.random.uniform()
            # print((purana_cost - naya_cost))
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


plt.plot(np.arange(epochs), costs)
plt.xlabel('Epochs')
plt.ylabel('Cost')
plt.show()
