import itertools as itera
import numpy as np
result = dict.fromkeys((i,j,k) for (i,j,k) in itera.product(list(range(0, 0x10)),list(range(0, 0x10)),list(range(0, 0x2))))

for i in range(0, 16):
    for j in range(0, 16):
        #result[(i,j,0x0)] = i+j
        #result[(i,j,0x1)] = i-j
        #print('{:05b}'.format(i+j))
        #print('{:05b}'.format(i+(~j+1)))
        print(np.binary_repr(i+j, width = 5))
        print(np.binary_repr(i-j, width = 5))
        #for k in range(0, 0x2):
        #    if (k == 0x0):

        #    if (k == 0x1):

#print(result[(i,j,k)] for (i,j,k) in itera.product(list(range(0, 0x10)),list(range(0, 0x10)),list(range(0, 0x2))))
