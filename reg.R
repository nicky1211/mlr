#Scatter Plot
#lm model
#summary
#Hypothesis
#Testing a subset of variables using a partial F-test(anova)
#. Confidence and Prediction Intervals
eruption.lm = lm(eruptions ~ waiting, data=faithful)
aov(eruption.lm)
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

reduced = lm(Price ~ Size + Lot, data=Housing) # Reduced model
> full = lm(Price ~ Size + Lot + Bedrooms + Baths, data=Housing) # Full Model
> anova(reduced, full) # Compare the models
Analysis of Variance Table
Model 1: Price ~ Size + Lot
Model 2: Price ~ Size + Lot + Bedrooms + Baths
Res.Df RSS Df Sum of Sq F Pr(>F)
1 97 9.0756e+10
2 95 8.5672e+10 2 5083798629 2.8186 0.06469 .
---
  Signif. codes: 0 „***‟ 0.001 „**‟ 0.01 „*‟ 0.05 „.‟ 0.1 „ ‟ 1
