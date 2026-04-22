# Program - pie chart to show cars data using Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

car_data = {
    "Fuel_Type": [
        "Petrol", "Diesel", "CNG", "Petrol", "Diesel", "Petrol", "CNG", "Petrol", "Diesel", "Petrol",
        "Diesel", "CNG", "Petrol", "Petrol", "Diesel", "CNG", "Petrol", "Diesel", "Petrol", "CNG",
        "Petrol", "Diesel", "Petrol", "CNG", "Petrol", "Diesel", "CNG", "Petrol", "Diesel", "Petrol",
    ]
}

df = pd.DataFrame(car_data)
fuel_counts = df["Fuel_Type"].value_counts()

colors = ["#ff9999", "#66b3ff", "#99ff99"]
explode = [0.05] + [0] * (len(fuel_counts) - 1)

plt.figure(figsize=(8, 8))
plt.pie(
    fuel_counts,
    labels=fuel_counts.index,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    shadow=True,
    startangle=140,
    textprops={"fontsize": 12},
)
plt.title("Car Distribution by Fuel Type", fontsize=16, fontweight="bold")
plt.axis("equal")
plt.tight_layout()
plt.show()
