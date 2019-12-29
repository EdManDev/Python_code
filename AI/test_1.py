print("\033c")

# import tensorflow as tf
# print(tf.__version__)

# SIMPLE LINEAR REGRETION

# import the relevant libraries

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random input data to train on



observations = 1000

xs=np.random.uniform(low=-10,high=10,size=(observations,1))
zs=np.random.uniform(-10,10,(observations,1))

inputs = np.column_stack((xs,zs))

print (inputs.shape)