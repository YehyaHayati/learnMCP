---
tags:
  - AI-900
  - Azure
  - MLConcepts
  - Regression
  - SupervisedLearning
---
_Regression_ is a form of supervised machine learning in which the ==label predicted by the model is a numeric value==. For example:
- The number of ice creams sold on a given day, based on the temperature, rainfall, and windspeed.
- The selling price of a property based on its size in square feet, the number of bedrooms it contains, and socio-economic metrics for its location.
- The fuel efficiency (in miles-per-gallon) of a car based on its engine size, weight, width, height, and length.
The process for ==training a regression model (or indeed, any supervised machine learning model) involves multiple iterations in which you use an appropriate algorithm (usually with some parameterized settings) to train a model, evaluate the model's predictive performance, and refine the model by repeating the training process with different algorithms and parameters until you achieve an acceptable level of predictive accuracy==.
## Regression evaluation metrics
Based on the differences between the predicted and actual values, you can calculate some common metrics that are used to evaluate a regression model.
### Mean Absolute Error (MAE)
This metric is known as the _absolute error_ for each prediction, and can be summarized for the whole validation set as the **mean absolute error** (MAE). ==The mean absolute error metric takes all discrepancies between predicted and actual labels into account equally.== 
In the ice cream example, the mean (average) of the absolute errors (2, 3, 3, 1, 2, and 3) is **2.33**.
### Mean Squared Error (MSE)
Sometimes, ==it may be more desirable to have a model that is consistently wrong by a small amount than one that makes fewer, but larger errors==. One way to produce a metric that "amplifies" larger errors by _squaring_ the individual errors and calculating the mean of the squared values. This metric is known as the **mean squared error** (MSE). The mean squared error ==helps take the magnitude of errors into account, but because it _squares_ the error values, the resulting metric no longer represents the quantity measured by the label==.
In our ice cream example, the mean of the squared absolute values (which are 4, 9, 9, 1, 4, and 9) is **6**. 
In other words, we can say that the MSE of our model is 6, ==but that doesn't measure its accuracy in terms of the number of ice creams that were mispredicted==; 6 is just a numeric score that indicates the level of error in the validation predictions.
### Root Mean Squared Error (RMSE)
If we want to measure the error in terms of the number of ice creams, we need to calculate the _square root_ of the MSE; which produces a metric called, unsurprisingly, **Root Mean Squared Error**. In this case √6, which is **2.45** (ice creams).
### Coefficient of determination (R2)
==All of the metrics so far compare the discrepancy between the predicted and actual values in order to evaluate the model.== However, in reality, there's some natural random variance in the daily sales of ice cream that the model takes into account. In a linear regression model, the training algorithm fits a straight line that minimizes the mean variance between the function and the known label values. ==The **coefficient of determination** (more commonly referred to as $R^2$ or **R-Squared**) is a metric that measures the proportion of variance in the validation results that can be explained by the model, as opposed to some anomalous aspect of the validation data== (for example, a day with a highly unusual number of ice creams sales because of a local festival).
The calculation for R2 is more complex than for the previous metrics. It compares the sum of squared differences between predicted and actual labels with the sum of squared differences between the actual label values and the mean of actual label values, like this:
$$R^2 = 1- \frac{\sum(y-ŷ)^2}{\sum(y-ȳ)^2}$$
The result is a value between 0 and 1 that describes the proportion of variance explained by the model. In simple terms, ==the closer to 1 this value is, the better the model is fitting the validation data.== In the case of the ice cream regression model, the R2 calculated from the validation data is **0.95**.