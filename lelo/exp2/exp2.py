# Implementation of Linear Regression in python
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Step 1 & 2: Import libraries and define custom dataset
X = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38])
Y = np.array([19, 21, 23, 25, 27, 29, 31, 33, 35, 37])

# Step 4: Calculate slope and y-intercept using Least Squares Method
mean_X, mean_Y = np.mean(X), np.mean(Y)
slope = np.sum((X - mean_X) * (Y - mean_Y)) / np.sum((X - mean_X) ** 2)
y_intercept = mean_Y - slope * mean_X
Y_pred = slope * X + y_intercept

print(f"Slope (m): {slope:.4f}")
print(f"Y-intercept (c): {y_intercept:.4f}")

# Step 5: Plotting the line of best fit
plt.scatter(X, Y, color="blue", alpha=0.5, label="Actual Data")
plt.plot(
    X, Y_pred, color="red", linewidth=2, label=f"Y = {slope:.2f}X + {y_intercept:.2f}"
)
plt.xlabel("Max Temperature (°C)")
plt.ylabel("3PM Temperature (°C)")
plt.title("Linear Regression - MaxTemp vs Temp3pm")
plt.legend()
plt.grid(True, alpha=0.3)
output_path = Path(__file__).resolve().parent / "linear_regression_plot.png"
plt.savefig(output_path, dpi=150)
print(f"Plot saved to: {output_path}")

# Step 6: Model Evaluation (RMSE and R-squared)
rmse = np.sqrt(np.mean((Y - Y_pred) ** 2))
r_squared = 1 - np.sum((Y - Y_pred) ** 2) / np.sum((Y - mean_Y) ** 2)
print(f"RMSE: {rmse:.4f}")
print(f"R-squared: {r_squared:.4f}")
