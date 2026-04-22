# Write a R program to demonstrate use of plotly library.
library(plotly)

# Plot 1: Scatter Plot - MPG vs Horsepower
p1 <- plot_ly(mtcars, x = ~hp, y = ~mpg, color = ~factor(cyl),
              type = "scatter", mode = "markers",
              marker = list(size = 8)) %>%
  layout(title = "Scatter Plot: MPG vs Horsepower",
         xaxis = list(title = "Horsepower"),
         yaxis = list(title = "Miles per Gallon"))
p1

# Plot 2: Bar Chart - Count of Cars by Cylinder
cyl_counts <- as.data.frame(table(mtcars$cyl))
colnames(cyl_counts) <- c("Cylinders", "Count")
p2 <- plot_ly(cyl_counts, x = ~Cylinders, y = ~Count, type = "bar",
              color = ~Cylinders) %>%
  layout(title = "Bar Chart: Cars by Cylinder Count",
         xaxis = list(title = "Cylinders"),
         yaxis = list(title = "Count"))
p2

# Plot 3: Histogram - Distribution of Horsepower
p3 <- plot_ly(mtcars, x = ~hp, type = "histogram",
              marker = list(color = "steelblue", line = list(color = "white", width = 1))) %>%
  layout(title = "Histogram: Horsepower Distribution",
         xaxis = list(title = "Horsepower"),
         yaxis = list(title = "Frequency"))
p3

# Plot 4: Box Plot - MPG by Cylinder Group
p4 <- plot_ly(mtcars, x = ~factor(cyl), y = ~mpg, type = "box",
              color = ~factor(cyl)) %>%
  layout(title = "Box Plot: MPG by Cylinders",
         xaxis = list(title = "Cylinders"),
         yaxis = list(title = "Miles per Gallon"))
p4

# Plot 5: Pie Chart - Cars by Cylinder
p5 <- plot_ly(cyl_counts, labels = ~Cylinders, values = ~Count, type = "pie",
              textinfo = "label+percent") %>%
  layout(title = "Pie Chart: Cars by Cylinder Count")
p5
