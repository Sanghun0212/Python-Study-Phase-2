## Day 5

import os  ## OS means operating system --> import os helps to heal with os functions
import math
import matplotlib.pyplot as plt

v0 = 50
g = 9.81
dt = 0.005

k = 0.002
m = 1.0

angles =[30, 45, 60]
colors = ["tab:blue", "tab:blue", "tab:red"]

ranges_drag = []

def simulate_with_drag(angle_deg):

    vx = v0 * math.cos(math.radians(angle_deg))
    vy = v0 * math.sin(math.radians(angle_deg))

    x, y = 0, 0 

    xs, ys = [x], [y]

    while y >= 0.0:
        v = math.hypot(vx, vy)   ## hypot() --> calculate hypotenuse
        ax = -(k/m) * v * vx
        ay = -g - (k/m) * v * vy

        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        xs.append(x)
        ys.append(y)

    return xs, ys


def simulate_nodrag_45():
    vx = v0 * math.cos(math.radians(45))
    vy = v0 * math.sin(math.radians(45))

    x, y = 0, 0
    xs, ys = [x], [y]

    while y >= 0:
        vy += -g * dt
        x += vx * dt
        y += vy * dt
        xs.append(x)
        ys.append(y)

    return xs, ys ## This makes xs can collect values outside of the while loop

plt.figure()
for ang, c in zip(angles, colors):
    x_list, y_list = simulate_with_drag(ang)
    ranges_drag.append(x_list[-1])
    plt.plot(x_list, y_list, label = "{ang} degree with drag", color = c)

x_ref, y_ref = simulate_nodrag_45()
plt.plot(x_ref, y_ref, "--", label="45° (no drag)", color="black", linewidth=1.5)

print("=== Ranges with Drage (k=0.002, m=1.0) ===")
for ang, r in zip(angles, ranges_drag):
    print(f"Angle: {ang:2d} degree --> Range: {r:.3f} m")

plt.title("Projectile with Air Resistance: Angle Comparison")    
plt.xlabel("Horizontal Distance")
plt.ylabel("Height (m)")
plt.grid(True)
plt.legend()
plt.show()

out_dir = "images"
os.makedirs(out_dir, exist_ok = True)  ## mean: make 'out_dir' folder but if the folder exist you can just skip
