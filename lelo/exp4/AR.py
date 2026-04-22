import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_absolute_error

# Load your data
data = pd.read_csv('weather.csv')['MaxTemp']

# Your current AR script only needs one column from a CSV: MaxTemp.
# So you can create your own dataset as long as:

# It is a .csv file.
# It has a column named exactly MaxTemp.
# Values are numeric (temperature numbers), no text.

# Split: 80% train, 20% test
train_size = int(len(data) * 0.8)
train = data[:train_size]
test = data[train_size:]

# Fit AR model
model = AutoReg(train, lags=2, old_names=False).fit()
forecast = model.predict(start=len(train), end=len(data)-1)

# Calculate only overall accuracy
mae = mean_absolute_error(test, forecast)
mean_temp = test.mean()
accuracy = (1 - (mae / mean_temp)) * 100

print(f"Overall Accuracy: {accuracy:.2f}%")

# ===== PLOT =====
plt.figure(figsize=(10, 4))
plt.plot(range(len(train)), train, label='Train', marker='o', markersize=3)
plt.plot(range(len(train), len(data)), test, label='Actual', marker='o', markersize=4, color='green')
plt.plot(range(len(train), len(data)), forecast, label='AR Forecast', marker='x', linestyle='--', color='red')
plt.xlabel('Day')
plt.ylabel('Max Temperature (°C)')
plt.legend()
plt.title('AR Model - MaxTemp Forecast')
plt.tight_layout()
plt.show()
