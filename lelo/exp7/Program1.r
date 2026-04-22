# Write a R program to demonstrate use of the ggplot library.
library(ggplot2)
library(gridExtra)

# Using built-in 'mtcars' and 'iris' datasets
head(mtcars)
head(iris)

# Plot 1: Scatter Plot - MPG vs Horsepower
p1 <- ggplot(mtcars, aes(x = hp, y = mpg, color = factor(cyl))) +
  geom_point(size = 3) +
  labs(title = "Scatter Plot: MPG vs Horsepower", x = "Horsepower", y = "MPG", color = "Cylinders") +
  theme_minimal()
print(p1)

# Plot 2: Bar Chart - Count of Cars by Cylinder Type
p2 <- ggplot(mtcars, aes(x = factor(cyl), fill = factor(cyl))) +
  geom_bar() +
  labs(title = "Bar Chart: Cars by Cylinder Count", x = "Cylinders", y = "Count", fill = "Cylinders") +
  theme_classic()
print(p2)

# Plot 3: Histogram - Distribution of Horsepower
p3 <- ggplot(mtcars, aes(x = hp)) +
  geom_histogram(binwidth = 25, fill = "steelblue", color = "white") +
  labs(title = "Histogram: Horsepower Distribution", x = "Horsepower", y = "Frequency") +
  theme_minimal()
print(p3)

# Plot 4: Box Plot - MPG by Cylinder Group
p4 <- ggplot(mtcars, aes(x = factor(cyl), y = mpg, fill = factor(cyl))) +
  geom_boxplot() +
  labs(title = "Box Plot: MPG by Cylinders", x = "Cylinders", y = "MPG", fill = "Cylinders") +
  theme_light()
print(p4)

# Plot 5: Line Chart - MPG vs Weight with Regression Line
p5 <- ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point(color = "darkblue", size = 2) +
  geom_smooth(method = "lm", col = "red", se = TRUE) +
  labs(title = "Line Chart: MPG vs Weight (with Regression)", x = "Weight (1000 lbs)", y = "MPG") +
  theme_bw()
print(p5)

# Plot 6: Density Plot - Sepal Width Distribution
p7 <- ggplot(iris, aes(x = Sepal.Width, fill = Species)) +
  geom_density(alpha = 0.5) +
  labs(title = "Density Plot: Sepal Width by Species", x = "Sepal Width", y = "Density") +
  theme_light()
print(p7)

# Plot 7: Pie Chart - Cars by Cylinder (using bar + coord_polar)
cyl_counts <- as.data.frame(table(mtcars$cyl))
colnames(cyl_counts) <- c("Cylinders", "Count")
p8 <- ggplot(cyl_counts, aes(x = "", y = Count, fill = Cylinders)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  labs(title = "Pie Chart: Cars by Cylinder Count") +
  theme_void()
print(p8)

# Plot 8: Stacked Bar Chart - Cylinder vs Transmission
p9 <- ggplot(mtcars, aes(x = factor(cyl), fill = factor(am))) +
  geom_bar(position = "stack") +
  labs(title = "Stacked Bar: Cylinders vs Transmission", x = "Cylinders", y = "Count", fill = "Transmission\n(0=Auto,1=Manual)") +
  theme_classic()
print(p9)

# Plot 9: Faceted Scatter Plot by Transmission Type
p10 <- ggplot(mtcars, aes(x = hp, y = mpg, color = factor(cyl))) +
  geom_point(size = 2.5) +
  facet_grid(. ~ am, labeller = labeller(am = c("0" = "Automatic", "1" = "Manual"))) +
  labs(title = "Faceted Plot: MPG vs HP by Transmission", x = "Horsepower", y = "MPG", color = "Cylinders") +
  theme_gray()
print(p10)

# Combined grid view of all basic plots
grid.arrange(p1, p2, p3, p4, p5, p7, p8, ncol = 2)
