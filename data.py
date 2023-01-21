import numpy as np

def getarray():
    return array

# array = np.random.randint(100001,999999,2000)

# for item in array:
#     with open('data.txt','a') as f:
#         f.write(str(item))
#         f.write(',')
        

with open('data.txt','r') as f:
    array = f.read().rstrip(',').split(',')
    array = [int(item) for item in array]
    array = np.array(array)
