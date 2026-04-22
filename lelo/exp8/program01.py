# Program 1- Scatter plot (create or upload any suitable data s
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather_data = {
    "MinTemp": [
        12.4, 15.0, 10.2, 8.5, 18.1, 21.3, 14.6, 9.8, 16.2, 11.1,
        7.3, 13.5, 19.0, 22.4, 5.9, 17.8, 20.1, 6.7, 24.0, 9.2,
        14.1, 16.9, 3.8, 11.7, 18.9, 25.2, 8.9, 13.0, 21.7, 4.5,
    ],
    "MaxTemp": [
        23.1, 27.8, 19.4, 16.7, 30.2, 34.1, 24.0, 18.5, 28.9, 20.3,
        14.8, 22.6, 31.0, 36.5, 12.1, 29.4, 33.2, 15.3, 38.0, 17.6,
        25.1, 27.2, 10.9, 21.0, 30.1, 39.3, 16.4, 23.5, 35.0, 11.8,
    ],
    "RainToday": [
        "No", "No", "Yes", "Yes", "No", "No", "Yes", "Yes", "No", "Yes",
        "Yes", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes",
        "No", "No", "Yes", "Yes", "No", "No", "Yes", "No", "No", "Yes",
    ],
}

df = pd.DataFrame(weather_data)

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x="MinTemp", y="MaxTemp", hue="RainToday", data=df, alpha=0.7, edgecolor=None
)
plt.title("Scatter Plot: Min Temperature vs Max Temperature")
plt.xlabel("Minimum Temperature (°C)")
plt.ylabel("Maximum Temperature (°C)")
plt.legend(title="Rain Today")
plt.grid(True, alpha=0.3)
plt.show()