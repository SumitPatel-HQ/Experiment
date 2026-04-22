# Multiple Linear Regression in Python

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = [
	[2, 60],
	[3, 65],
	[4, 70],
	[5, 75],
	[6, 80],
	[7, 85],
	[8, 90],
]
y = [35, 42, 50, 58, 66, 74, 82]

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

new_data = [[6, 78]]
prediction = model.predict(new_data)
print("Predicted score:", prediction[0])

plt.figure(figsize=(7, 5))
plt.scatter(y, y_pred, color="blue")
plt.title("Actual vs Predicted Scores")
plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.show()
