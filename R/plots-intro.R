dim(iris)
head(iris)
str(iris)
summary(iris)

hist(iris$Sepal.Length)
hist(iris$Petal.Length)

plot(iris$Species)             # plotting categorical values
plot(iris$Sepal.Length)        # plotting numerical values
plot(iris$Petal.Length, col = iris$Species)
plot(iris$Petal.Length, iris$Petal.Width)

plot(iris$Petal.Length, iris$Petal.Width, col = iris$Species)
plot(iris$Sepal.Length, iris$Sepal.Width, col = iris$Species)