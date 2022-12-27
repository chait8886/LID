import numpy as np

data = np.load('./data/lid_mnist_fgsm.npy')



print(data[0])

partition = 9788

print(data[partition*2])
print(data[partition*3 -1])