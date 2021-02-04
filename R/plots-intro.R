?datasets
library( help = "ISLR")
library(help = "datasets")
?iris

write.csv(iris, "iris.csv")
iris3

dim(iris)
head(iris)
str(iris)

?is.na
length(is.na(iris))
sum(is.na(iris))
iris[is.na(iris),]

summary(iris)

hist(iris$Sepal.Length)
hist(iris$Petal.Length)
hist(iris$Petal.Length[iris$Species != "setosa"])

plot(iris$Species)             # plotting categorical values
plot(iris$Sepal.Length)        # plotting numerical values
plot(iris$Sepal.Length, col = iris$Species) 
plot(iris$Petal.Length, col = iris$Species)

plot(iris$Petal.Length, iris$Petal.Width)

plot(iris$Petal.Length, iris$Petal.Width, col = iris$Species)
plot(iris$Sepal.Length, iris$Sepal.Width, col = iris$Species)


attach(iris)
plot(Species)
detach(iris)
