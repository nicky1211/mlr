library(readr)
dataset <- read_csv(NULL)


logitMod <- glm(ABOVE50K ~ RELATIONSHIP + AGE + CAPITALGAIN + OCCUPATION + EDUCATIONNUM, data=adult, family=binomial(link="logit"))

confint.default(logitMod)
wald.test(b = coef(logitMod), Sigma = vcov(logitMod), Terms = 4:6)
predicted <- plogis(predict(logitMod, adult))  # predicted scores
# or
predicted <- predict(logitMod, adult, type="response")  # predicted scores



library(InformationValue)
optCutOff <- optimalCutoff(adult$ABOVE50K, predicted)[1] 


summary(logitMod)

vif(logitMod)

misClassError(adult$ABOVE50K, predicted, threshold = optCutOff)

plotROC(adult$ABOVE50K, predicted)
sensitivity(adult$ABOVE50K, predicted, threshold = optCutOff)
specificity(adult$ABOVE50K, predicted, threshold = optCutOff)
confusionMatrix(adult$ABOVE50K, predicted, threshold = optCutOff)

#Odds Ratio
OR <- exp(fit$coefficient[2])
