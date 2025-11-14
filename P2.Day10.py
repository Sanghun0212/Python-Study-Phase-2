## Day 10 pendulum with air resisrance

# theta = degree
# w = angular velocity 
# b = damping coefficient
# mass of pendulum

import math
import matplotlib.pyplot as plt

g = 9.81
L = 1.0
m = 1.0
b = 0.2
dt = 0.01

theta_1 = math.radians(30)
theta_2 = math.radians(60)

t = 0
w_1, w_2 = 0, 0
alpha_1, alpha_2 = 0, 0

theta_1_list = []
theta_2_list = []
time_list = []

for _ in range(3000):
    # alpha += -b/m * w - g/L * math.sin(theta) --> have to erase + 
    alpha_1 = -b/m * w_1 - g/L * math.sin(theta_1)
    w_1 += alpha_1 * dt
    theta_1 += w_1 * dt

    alpha_2 = -b/m * w_2 - g/L * math.sin(theta_2)
    w_2 += alpha_2 * dt
    theta_2 += w_2 * dt

    t += dt

    theta_1_list.append(theta_1)
    theta_2_list.append(theta_2)
    time_list.append(t)

plt.plot(time_list, theta_1_list, label = "30 degree")
plt.plot(time_list, theta_2_list, label="60 degree")
plt.title("Pendulum work with air resistance 30 & 60 degrees")
plt.xlabel("Time(s)")
plt.ylabel("Theta(rad)")
plt.legend()
plt.grid()
plt.show()