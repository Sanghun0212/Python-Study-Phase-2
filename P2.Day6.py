
## Day 6

import os
import math
import csv
import matplotlib.pyplot as plt

v0 = 50.0
g = 9.81
dt = 0.01
k = 0.002
m = 1.0

angles = [30, 45, 60]
colors = ["tab:blue", "tab:green", "tab:red"]

def simulate_with_drag(angle_deg):

    vx = v0 * math.cos(math.radians(angle_deg))
    vy = v0 * math.sin(math.radians(angle_deg))

    x, y = 0.0, 0.0
    xs, ys = [x], [y]
    t = 0.0

    while y >= 0 :
        v = math.hypot(vx, vy)
        ax = -(k/m) * v * vx
        ay = -g -(k/m) * v * vy

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt
        t += dt

        xs.append(x)
        ys.append(y)

    flight_time = t
    max_height = max(ys)
    flight_range = xs[-1]

    return flight_time, max_height, flight_range, xs, ys

os.makedirs("data", exist_ok = True)
os.makedirs("images", exist_ok = True)

csv_path = "data/day6_results.csv"          ## This is a address of csv file
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    # open():  opening file
    # "w": writing mode
    # "encoding = "utf-8"
    # newline="": change the line
    # as file: give a name on the opened file
    writer = csv.writer(file)  ## respone the 'writer' to use order 'writer.writerow()'
    writer.writerow(["Angle (deg)", "Flight Time (s)", "Max Height (m)", "Range (m)"])
    ## colums of the csv file
    for angle, color in zip(angles, colors):
        flight_time, max_height, flight_range, xs, ys = simulate_with_drag(angle)
        writer.writerow([angle, round(flight_time, 2), round(max_height, 2), round(flight_range, 2)])

        plt.plot(xs, ys, label=f"{angle}", color = color)

        print(f"Simulation data saved to '{csv_path}'")

plt.title("Projectile with Air Resistance (Saved Results)")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.legend()
plt.grid(True)
plt.show()       