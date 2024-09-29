import numpy as np 


arr = np.random.randint(1,10,(3,2))
print(arr.shape)
# print(arr.reshape(1,6))
print(np.reshape(arr,(2,3),'C'))
print(np.reshape(arr,(2,3),'F'))
print(np.reshape(arr,(2,3),'A'))