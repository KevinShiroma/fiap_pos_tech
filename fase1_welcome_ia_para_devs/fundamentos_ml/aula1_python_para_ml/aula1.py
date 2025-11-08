import numpy as np


data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mean = np.mean(data)
# print(mean)

# from scipy.integrate import solve_ivp
# def dydt(t, y):
#    return -0.5 * y
# solution = solve_ivp(dydt, [0, 10], [2])
# print(solution.y)

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.show()