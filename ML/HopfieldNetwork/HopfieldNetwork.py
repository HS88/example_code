import numpy as np
from PIL import Image
import random

def mat2vec(x):
    m = x.shape[0]*x.shape[1]
    tmp1 = np.zeros(m)

    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i,j]
            c +=1
    return tmp1

def array2img(data, outFile = None):
    #data is 1 or -1 matrix
    y = np.zeros(data.shape,dtype=np.uint8)
    y[data==1] = 255
    y[data==-1] = 0
    img = Image.fromarray(y,mode="L")
    if outFile is not None:
        img.save(outFile)
    return img

def mat2vec(x):
    m = x.shape[0]*x.shape[1]
    tmp1 = np.zeros(m)
    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i,j]
            c +=1
    return tmp1

train_img = Image.open('Train.png')
train_img = train_img.convert(mode="L")
I = np.asarray( train_img , dtype=np.uint8) # pixel array from image
x = np.zeros( I.shape,dtype=np.float)
x[ I > 145 ] = 1
x[x == 0] = -1
vec = mat2vec(x)
# now I have matrix for two classes in my image, I will convert it into vector now
w = np.zeros([len(vec),len(vec)])

for i in range(len(vec)):
    for j in range(i,len(vec)):
        if i == j:
            w[i,j] = 0
        else:
            w[i,j] = vec[i] * vec[j]
            w[j,i] = w[i,j]

test_img = Image.open('Test2.png')
test_img = test_img.convert(mode="L")

I_test = np.asarray( test_img , dtype=np.uint8) # pixel array from image
x_test = np.zeros( I_test.shape,dtype=np.float)
x_test[ I_test > 145 ] = 1
x_test[x_test == 0] = -1

output  =  x_test.shape
#saved = array2img(x_test,"fromcode.png")

#pick random pixel and update it.
# i will run it for 100000 times
for k in range(50000):
    i = random.randint(0,len(x_test[0])-1)
    j = random.randint(0,len(x_test[i])-1)
    #  x_test[i][j] is random node for which we will adjust the node value
    sum = 0;
    weight_index = i*len(x_test)+j; # this is the index of w matrix. For each node i,j in pixel array, we need to find
                                    # the weight of each node. As the weight matrix is (pixel[x]*pixel[y],pixel[x]*pixel[y] )
                                    # dimension, we will need to find the corresponding row with this formula and then
                                    # need to multiply each test pixel with coresponding weight

    for u in range(x_test.shape[0]):
        for e in range(x_test.shape[1]):
            node_value = x_test[u,e]
            sum = sum + ( node_value * w[i*len(x_test)+j][u*len(x_test)+e])

    if sum - 0.5 > 0:
        x_test[i][j] = 1
    else:
        x_test[i][j] = -1

output  =  x_test.shape
saved = array2img(x_test,"fromcode2.png")