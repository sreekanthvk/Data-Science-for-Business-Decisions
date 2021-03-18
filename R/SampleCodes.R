x <- rnorm(1000)
x2 <- x + 1
y <- 3 * x + 2
df <- data.frame(x1=x, x2=x2, y=y)

fit <- glm(y~x1, data = df)
summary(fit)

fit2 <- glm(y~x1+x2, data = df)
summary(fit2)

install.packages("swirl")
library(swirl)
swirl::swirl()


library(tidyverse)
library(reshape2)
library(ggthemes)
library(gganimate)
library(gifski)

covid.data <- read.csv("D:\Learning\Data-Science-for-Business-Decisions\Data\archive\full_grouped.csv")


library(ISLR)
library(help=ISLR)
head(Hitters)
hist(Hitters$Salary)
hist(log(Hitters$Salary))
# detach(Hitters)
dat <- Hitters
dat$Type = 1 
dat$Type[dat$Years >= 4.5 & dat$Hits < 117.5] <- 2
dat$Type[dat$Years >= 4.5 & dat$Hits >= 117.5] <- 3
dat$Type <- as.factor(dat$Type)
# detach(dat)
dat <- dat[,c("Hits", "Years", "Salary", "Type")]
attach(dat)
plot(Years, Hits, col = Type)

plot(iris$Petal.Length, iris$Petal.Width, col = iris$Species)



te <- seq(0.001,.999, 0.001)

aofs <- 0.5 * log((1-te)/te)

expo <- exp(aofs)
negexpo <- exp(-1*aofs)

plot(te,aofs)

plot(aofs,expo)
plot(aofs,negexpo)
# plot(aofs,te)

0.5 * log((1 - (1/8))/(1/8))
