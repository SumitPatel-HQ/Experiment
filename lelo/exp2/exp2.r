#User define Data set 
X <- c(1,2,3,4,5)
y <- c(12,19,29,37,45)

data <- data.frame(X,y)
#print(data)

# Regression Model
model <- lm(y ~ X, data = data)

# Slope and Intercept m & b
intercept <- coef(model)[1]
slope <- coef(model)[2]

#new data Point (X) and its predicted value (y)
new_data <- data.frame(X = 6)
y_new <- predict(model, new_data)

#printing the values m & b & y_new
cat("Slope (m):", slope,"\n")
cat("Intercept (b):", intercept,"\n")
cat("Predicted value (X = 6) :", y_new,"\n")

#ploting the graph
plot(X,y,
     main = "Simple Linear Regression",
     xlab = "Year",
     ylab = "Expenditure",
     pch = 16,
     xlim = c(1,7),
     ylim = c(10,80)
     )

#Regression line
abline(model, col = "blue")

points(6, y_new, pch = 16, col = "red")

#Display slope and intercept on graph 
text(3,80,
     labels= paste("y = ",round(slope,2), "X + ",round(intercept,2)),
     col = "darkgreen"
     )


