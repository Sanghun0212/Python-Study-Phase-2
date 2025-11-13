# Day 7: import csv files
import pandas as pd
import matplotlib.pyplot as plt
import os

# ----- File path -----
csv_path = "data/day6_results.csv"

# ----- Load CSV data -----
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)   ## This is order to import the csv file to here
    print(" CSV file loaded successfully!")
else:
    raise FileNotFoundError("❌ CSV file not found. Run Day 6 simulation first!")
## raise --> if there is no file on it stop the program with FileNotFoundError code
# ----- Display data -----
print("\n=== Simulation Data ===")
print(df)
print("\n=== Data Summary ===")
print(df.describe())
## .describe shows number coulmns with statistics values suchas count, means, std, ...
## the value from the data shows 25% and 50% 75% is calculated by linear expectation eventhough there is no actual data we put on each percent
# ----- Plot data -----
plt.figure(figsize=(8,5))
plt.plot(df["Angle (deg)"], df["Range (m)"], marker="o", label="Range (m)")
plt.plot(df["Angle (deg)"], df["Max Height (m)"], marker="s", label="Max Height (m)")
plt.plot(df["Angle (deg)"], df["Flight Time (s)"], marker="^", label="Flight Time (s)")

plt.title("Projectile Data Analysis")
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()

os.makedirs("images", exist_ok=True)
plt.savefig("images/day7_analysis_plot.png", dpi=300)
plt.show()