#Step 1: Creating Data set
X1 <- c(4,3,1.6,1.2,3.4,4.8,6)
X2 <- c(1.5,2.2,1,2,0.8,1.6,1.9)
Y <- c(160,112,69,90,123,186,56)

# Step 2: Create data frame
data <- data.frame(X1, X2, Y)

# Step 3: Fit regression model
model <- lm(Y ~ X1 + X2, data = data)

# Step 4: Extract coefficients
a <- coef(model)[1]
b1 <- coef(model)[2]
b2 <- coef(model)[3]

# Step 5: Display coefficients
cat("Intercept (a)=", a,"\n")
cat("Coefficient b1=",b1,"\n")
cat("Coefficient b2=",b2,"\n\n")

# Step 6: Display regression equation
cat("Regression Equation:\n")
cat("Y =",round(a,3),"+",round(b1,3),"* X1+",round(b2,3),"* X2\n\n")

# Step 7: Prediction using equation
X1_new <- 1.5
X2_new <- 3
Y_pred <- a + b1*X1_new + b2*X2_new

# Step 8: Display predicted value
cat("Predicted Damage Price = Rs.", round(Y_pred,3),"\n")