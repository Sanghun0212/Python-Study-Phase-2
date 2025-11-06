## Day 4
import matplotlib.pyplot as plt
import math

v0 = 50
g = 9.81
dt = 0.01

angles = [30, 45, 60]
colors = ["blue", "green", "red"]

ranges = []  # The reason that I put ranges = [] outside of the loop is because it need to collect data not disapearing after the one cycle of loop

for angle, color in zip(angles, colors):    ## This zip can be used for pairing angles and color variables
    vx = v0 * math.cos(math.radians(angle))
    vy = v0 * math.sin(math.radians(angle))
    x, y, t = 0.0, 0.0, 0.0

    x_list, y_list = [x], [y]

    while y >= 0.0:
        vy += -g * dt
        x += vx * dt
        y += vy * dt
        t += dt

        x_list.append(x)
        y_list.append(y)

    flight_range = x_list[-1]
    ranges.append(flight_range)

    plt.plot(x_list, y_list, label = f"{angle} degrees", color = color)

print("=== Projectile Range by Angle ===")
for angle, r in zip (angles, ranges):
    print(f"angle: {angle:2d} degrees --> Range: {r:.2f} m")
## This match eaches angles to each right ranges
plt.title("Projectile Trajectories at Different Launch Angles") 
plt.xlabel("Horizontal Distance(m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.legend()
plt.show()

## From this loop, python calculate all process on one single angle and go to next angles