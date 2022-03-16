import PIL
import matplotlib.pyplot as plt
import numpy as np 

img = PIL.Image.open("lena.png")
gray_img = img.convert("L")
plt.imshow(gray_img, cmap='gray')

import numpy as np 
data=np.array(gray_img)

def generate_block(data, dim):
    mydim=np.zeros((dim*dim,4))
    newshape=data.shape[0]/dim
    count=0
    newdata=np.zeros(data.shape)
    for i in range(dim):
        for j in range(dim):
            mydim[count][0]=i*newshape
            mydim[count][1]=j*newshape
            mydim[count][2]=(i+1)*newshape
            mydim[count][3]=(j+1)*newshape
            count+=1
    return mydim

def jig_shuffle(data, mydim, dim):
    newshape=data.shape[0]/dim
    newdata = np.zeros(data.shape)
    permuted=np.arange(16)
    np.random.shuffle(permuted)

    for i in range(16):
        for j in range(0,int(newshape)):
            for k in range(0,int(newshape)):
                newdata[int(mydim[i][0])+j][int(mydim[i][1])+k]=data[int(mydim[permuted[i]][0])+j][int(mydim[permuted[i]][1])+k]
    return newdata

mydim = generate_block(data, 4)
d=jig_shuffle(data,mydim, 4)

new_image=np.array(d)
plt.imshow(new_image, cmap='gray')
plt.show()

def pixel_row_difference(a, b):
    return np.sum(a - b)

def pixel_col_difference(a, b):
    return np.sum(a - b)

def cost_function(data):
    data = np.array(data)
    padding_x = 75
    padding_y = 75
    total_dissimarity = 0

    for i in range(3):
        total_dissimarity += pixel_row_difference(data[:, (i+1)*padding_x-1], data[:, (i+1)*padding_x])
        total_dissimarity += pixel_col_difference(data[(i+1)*padding_x-1, :], data[(i+1)*padding_x, :])
    return total_dissimarity

epochs = 20
T = 30
factor = 0.995

purana_cost = cost_function(new_image)

for e in range(epochs):
    for t in range(10):
        a, b = np.random.randint(0, 16, size=2)

        permuted=np.arange(16)
        permuted[a], permuted[b] = permuted[b], permuted[a]
        image = np.zeros(data.shape)

        for i in range(16):
            for j in range(0,int(data.shape[0]/4)):
                for k in range(0,int(data.shape[0]/4)):
                    image[int(mydim[i][0])+j][int(mydim[i][1])+k]=new_image[int(mydim[permuted[i]][0])+j][int(mydim[permuted[i]][1])+k]

        naya_cost = cost_function(image)

        if naya_cost > purana_cost:
            permuted[a], permuted[b] = permuted[b], permuted[a]

        else:
            new_image = image
            purana_cost = naya_cost

    T = T*factor


plt.imshow(new_image, cmap='gray')
plt.show()