import PIL
import matplotlib.pyplot as plt
import numpy as np 

img = PIL.Image.open("lena.png")
gray_img = img.convert("L")
plt.subplot(1, 3, 1)
plt.imshow(gray_img, cmap='gray')

data= np.array(gray_img)

def generate_block(data):
    x, y = 75, 75
    print(x, y)
    img_block = []

    for i in range(4):
        for j in range(4):
            img_block.append(data[75*i:75+75*i, 75*j:75+75*j])
    return img_block


def mergeImages(data):
    f = np.hstack((data[0], data[1], data[2], data[3]))
    s = np.hstack((data[4], data[5], data[6], data[7]))
    t = np.hstack((data[8], data[9], data[10], data[11]))
    fo = np.hstack((data[12], data[13], data[14], data[15]))
    return np.vstack((f,s,t,fo))

def pixel_row_difference(a, b):
    sumn = 0
    for x, y in zip(a,b):
        sumn += np.abs(int(x) - int(y))
    return sumn

def pixel_col_difference(a, b):
    sumn = 0
    for x, y in zip(a,b):
        sumn += np.abs(int(x) - int(y))
    return sumn

def cost_function(data):
    data = np.array(data)
    padding_x = 75
    padding_y = 75
    total_dissimarity = 0
    for i in range(3):
        total_dissimarity += pixel_row_difference(data[:, (i+1)*padding_x-1], data[:, (i+1)*padding_x])
        total_dissimarity += pixel_col_difference(data[(i+1)*padding_x-1, :], data[(i+1)*padding_x, :])
    return total_dissimarity

d = np.array(generate_block(data))

ideal_cost = cost_function(mergeImages(d))

d = np.random.permutation(d)

epochs = 2000
T = 30
factor = 0.995
image = d[:]

# d= mergeImages(d)
# print(pixel_row_difference(d[:, 74], d[:, 75]))
plt.subplot(1, 3, 2)
plt.imshow(mergeImages(image), cmap='gray')

purana_cost = cost_function(mergeImages(d))
print(purana_cost)

for e in range(epochs):
    a, b = np.random.randint(0, 16, size=2)
    d[[a, b],:] = d[[b, a],:]
    naya_cost = cost_function(mergeImages(d))

    if np.abs(ideal_cost - naya_cost) > np.abs(ideal_cost - purana_cost):
        d[[a, b],:] = d[[b, a],:]

    else:
        image = d[:]
        purana_cost = naya_cost


print(purana_cost)
plt.subplot(1, 3, 3)
plt.imshow(mergeImages(image), cmap='gray')
plt.show()