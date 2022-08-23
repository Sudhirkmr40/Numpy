import numpy as np
import numpy.random

l = [1,2,3,4,5,6]
print(l)


l1 = [4,5,6,7,"sudhir", 34.54,True]
print(l1)
x=np.array(l1)
print(x)

a1 =np.array([[1,2,3,4],[455,5,42,4]])
print(a1)

a2  = np.array([[12,3,4,4],[4,234,5,53]])
print(a2)

print(a1.ndim)
print(a2.ndim)

a3 = np.array(([[1,2,4],[5,6,7],[8,9,10]]))
print(a3)
print(a3.ndim)

print(a3.shape)
print(a1.shape)

print(np.random.randint(2,10))


a4 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a4)
print(a4.ndim)
print(a4.shape)

x2 = np.random.randint(2,50,(2,3,4))

print(x2)

x3 = np.random.randn(2,3)
print(x3)

x3 = np.random.rand(2,3)
print(x3)

x4 = np.random .rand(4,4)
print(x4)

x5 = x4.reshape(1,2)
print(x5)


y = x6[2:4]
print(y)







l1 = [4,5,6,7,"sudhir", 34.54,True]
z = l1[::-1]
print(z)



