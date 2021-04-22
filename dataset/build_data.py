import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

directory = 'price_long_50'
filenames = os.listdir(directory)
print(filenames)

num_files=len(filenames)

all_data = np.zeros((num_files,2518),dtype = np.float32)
for i in range(num_files):
  filename = filenames[i]
  print(i)
  print(filename)
  
  data=pd.read_csv(directory+'/'+filename)
  vars = ['Open']
  data = data[vars]
  data = np.array(data)
  data = np.transpose(data)
  data = data[0]
  data = data[::-1]
  
  all_data[i] = data

print(all_data.shape)  
np.save('data',all_data)     
# save data in ndarray  
# 50 (n_stock rows), 2518 (n_days) 
# price from early to end, ith col represents ith day open price
