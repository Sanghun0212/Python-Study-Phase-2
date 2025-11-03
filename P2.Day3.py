## Day3 


import matplotlib.pyplot as plt
import math

v0 = 50
angle = 45
g = 9.81
dt = 0.01

vx = v0 * math.cos(math.radians(angle))
vy = v0 * math.sin(math.radians(angle))

x, y = 0.0, 0.0  ## reason that use 0.0 instead 0 is that 0 cannot show decimal numbers
t = 0.0

x_list, y_list, t_list = [0], [0], [0]

while y >= 0 : 
    vy += -g * dt
    x += vx * dt
    y += vy * dt
    t += dt

    x_list.append(x)
    y_list.append(y)
    t_list.append(t)


sim_time = t_list[-1]     # [-1] is the value that is located in last (front start with [0])
sim_max_y = max(y_list)
sim_range = x_list[-1]

th_time  = 2 * v0 * math.sin(math.radians(angle))
th_max_y = v0 ** 2 * math.sin(math.radians(angle)) ** 2 / 2 / g
th_range = v0 ** 2 * math.sin(math.radians(2 * angle)) /g 

print("=== Simulation vs Theoretical comparison ===")
print(f"Flight Time: {sim_time: .2f} s | Theory: {th_time: .2f} s")  # .2f means showing 2 decimal points
print(f"Max Height: {sim_max_y: .2f} m | Theory: {th_max_y: .2f} m") # have to use {something:.2f}
print(f"Flight Range: {sim_range: .2f} m | Theory: {th_range: .2f} m")

plt.plot(x_list, y_list, color ="blue", label = "Simulated Trajectory")
plt.title("Projectile Motion - Simulation vs Theory")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height(m)")
plt.grid(True)
plt.legend()
plt.show()


