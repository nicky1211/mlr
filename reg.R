eruption.lm = lm(eruptions ~ waiting, data=faithful)

newdata = data.frame(waiting=80)

predict(eruption.lm, newdata) 

summary(eruption.lm) 
As the p-value is much less than 0.05, we reject the null hypothesis that β = 0. Hence there is a significant relationship between the variables in the linear regression model of the data set faithful.

predict(eruption.lm, newdata, interval="confidence") 

predict(eruption.lm, newdata, interval="predict") 

plot(faithful$waiting, eruption.res, 
     ylab="Residuals", xlab="Waiting Time", 
          main="Old Faithful Eruptions") 

abline(0, 0)               

As the p-values of Air.Flow and Water.Temp are less than 0.05, they are both statistically significant in the multiple linear regression model of stackloss.

MLR
As the p-values of the hp and wt variables are both less than 0.05, neither hp or wt is insignificant in the logistic regression model.
