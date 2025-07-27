import matplotlib.pyplot as plt
import numpy as np

# graf lin. funkcie
y = [0,1,0,8,4,5,6,7]
plt.plot(y)
plt.show()

# graf kv.funkcie
x = np.arange(-2,2,0.01)
y = x**2
plt.plot(x,y)
plt.show()  