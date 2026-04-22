# ARIMA

# STEP 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

# STEP 2: Load dataset + build date index
df = pd.read_csv("weather.csv")
series = df["MinTemp"].astype(float)
series.index = pd.date_range("2020-01-01", periods=len(series), freq="D")
series.index.name = "Date"

# STEP 3: Stationarity-based differencing decision
d = 0 if adfuller(series, autolag="AIC")[1] <= 0.05 else 1

# STEP 4: Train-test split
split = int(len(series) * 0.8)
train, test = series[:split], series[split:]

# STEP 5: New logic -> auto-select best ARIMA(p,d,q) by AIC
best_order, best_fit, best_aic = None, None, np.inf
for p in range(3):
    for q in range(3):
        try:
            fit = ARIMA(train, order=(p, d, q)).fit()
            if fit.aic < best_aic:
                best_order, best_fit, best_aic = (p, d, q), fit, fit.aic
        except Exception:
            pass

if best_fit is None:
    raise ValueError("No ARIMA model could be fitted for the given data.")

# STEP 6: Forecast on test data
forecast = best_fit.get_forecast(steps=len(test))
forecast_mean = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# STEP 7: Visualize forecast vs actual
plt.figure(figsize=(12, 5))
plt.plot(train.index, train, label="Training Data", color="steelblue", linewidth=2)
plt.plot(test.index, test, label="Actual Test Data", color="green", linewidth=2)
plt.plot(
    test.index,
    forecast_mean,
    label="Forecasted Values",
    color="red",
    linestyle="--",
    linewidth=2,
    marker="o",
)
plt.fill_between(
    test.index,
    forecast_ci.iloc[:, 0],
    forecast_ci.iloc[:, 1],
    color="pink",
    alpha=0.4,
    label="95% Confidence Interval",
)
plt.title(f"ARIMA{best_order} — Forecast vs Actual", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

# STEP 8: Model accuracy (directional)
actual = test.values
predicted = forecast_mean.values
actual_diff = np.diff(actual)
predicted_diff = np.diff(predicted)
valid_mask = (actual_diff != 0) | (predicted_diff != 0)

if valid_mask.any():
    direction_match = np.sign(actual_diff[valid_mask]) == np.sign(
        predicted_diff[valid_mask]
    )
    model_accuracy = np.mean(direction_match) * 100
    accuracy_str = f"{model_accuracy:.2f}%"
else:
    accuracy_str = "N/A (no movement in actual and predicted series)"

print(f"Model Accuracy: {accuracy_str}")
