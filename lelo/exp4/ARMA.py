# AIM: Implementation of ARIMA Model in Python

# ── STEP 1: Import Libraries ──────────────────────────────
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error

# ── STEP 2: Load Dataset ──────────────────────────────────
series = pd.read_csv('timeseries_data.csv', parse_dates=['Date'], index_col='Date')['Value']

# This script in ARMA.py expects:

# CSV file name: timeseries_data.csv
# A date column named Date
# A numeric target column named Value
# So your custom CSV must look like this:

# Date,Value
# 2025-01-01,120
# 2025-01-02,123
# 2025-01-03,121
# 2025-01-04,126

# Notes:

# Date should be valid date text (YYYY-MM-DD is best).
# Value must be numeric.
# Keep rows in time order (oldest to newest).
# Avoid missing values if possible.

# ── STEP 3: Train-Test Split ──────────────────────────────
train_size = int(len(series) * 0.80)
train, test = series[:train_size], series[train_size:]

# ── STEP 4: Fit ARIMA Model ───────────────────────────────

p, d, q = 1, 1, 1    # ← Adjust based on ACF/PACF analysis

model = ARIMA(train, order=(p, d, q))
model_fit = model.fit()

# ── STEP 5: Forecast on Test Data ────────────────────────
forecast_steps = len(test)
forecast_result = model_fit.get_forecast(steps=forecast_steps)
forecast_mean   = forecast_result.predicted_mean
forecast_ci     = forecast_result.conf_int()

# ── STEP 6: Visualize Forecast ───────────────────────────
plt.figure(figsize=(12, 5))
plt.plot(train.index, train, label='Training Data', color='steelblue', linewidth=2)
plt.plot(test.index, test,   label='Actual Test Data', color='green', linewidth=2)
plt.plot(test.index, forecast_mean, label='Forecasted Values',
         color='red', linestyle='--', linewidth=2, marker='o')
plt.fill_between(test.index,
                 forecast_ci.iloc[:, 0],
                 forecast_ci.iloc[:, 1],
                 color='pink', alpha=0.4, label='95% Confidence Interval')
plt.title(f'ARIMA({p},{d},{q}) — Forecast vs Actual', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ── STEP 7: Overall Accuracy ─────────────────────────────
mae = mean_absolute_error(test, forecast_mean)
mean_value = test.mean()
accuracy = (1 - (mae / mean_value)) * 100

print(f"Overall Accuracy: {accuracy:.2f}%")