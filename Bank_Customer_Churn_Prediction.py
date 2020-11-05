#liabrary TTR
#library lubridate for manipulate date
#library ggplot2 for plot
#library dplyr for manipulate data
#library plyr for manipulate data
#library forecast for forecaste
#library plotly for plot
#library NbClust for clustering data
#libary mlbench for machine learning benchmark
#library glmnet for multiple regression
library("TTR")
library("lubridate")
library("ggplot2")
library("dplyr")
library("plyr")
library("forecast")
library("plotly")
library("NbClust")
library("mlbench")
library("glmnet")

#Load data
x<- "C:/Users/jessi/OneDrive/Desktop/ALY 6015/WK6 Final Project/data.csv"
df <- read.csv(file = x)
