---
tags:
  - AI-900
  - Azure
  - MLConcepts
  - Classification
  - SupervisedLearning
---
_Classification_ is a form of supervised machine learning in ==which the label represents a categorization, or _class_==. There are two common classification scenarios.
## Binary classification
In _binary classification_, the label determines whether the observed item _is_ (or _isn't_) an instance of a specific class. Or put another way, binary classification models predict one of two mutually exclusive outcomes. For example:
- Whether a patient is at risk for diabetes based on clinical metrics like weight, age, blood glucose level, and so on.
- Whether a bank customer will default on a loan based on income, credit history, age, and other factors.
- Whether a mailing list customer will respond positively to a marketing offer based on demographic attributes and past purchases.
In all of these examples, ==the model predicts a binary _true_/_false_ or _positive/negative_ prediction for a single possible class.==
## Multiclass classification
_Multiclass classification_ extends binary classification to ==predict a label that represents one of multiple possible classes.== For example,
- The species of a penguin (_Adelie_, _Gentoo_, or _Chinstrap_) based on its physical measurements.
- The genre of a movie (_comedy_, _horror_, _romance_, _adventure_, or _science fiction_) based on its cast, director, and budget.
To train a multiclass classification model, we need to ==use an algorithm to fit the training data to a function that calculates a probability value for each possible class==. There are two kinds of algorithm you can use to do this:
- One-vs-Rest (OvR) algorithms
- Multinomial algorithms
### One-vs-Rest (OvR) algorithms
One-vs-Rest algorithms ==train a binary classification function for each class==, each calculating the probability that the observation is an example of the target class. Each function calculates the probability of the observation being a specific class compared to _any_ other class. For our penguin species classification model, the algorithm would essentially create three binary classification functions:
- $f_0(x) = P(y=0 | x)$
- $f_1(x) = P(y=1 | x)$
- $f_2(x) = P(y=2 | x)$
Each ==algorithm produces a sigmoid function that calculates a probability value between 0.0 and 1.0.== A model trained using this kind of algorithm predicts the class for the function that produces the highest probability output.
### Multinomial algorithms
As an alternative approach is to use a multinomial algorithm, which ==creates a single function that returns a multi-valued output. The output is a _vector_ (an array of values) that contains the _probability distribution_ for all possible classes - with a probability score for each class which when totaled add up to 1.0==:
$$f(x) =[P(y=0|x), P(y=1|x), P(y=2|x)]$$
An example of ==this kind of function is a _softmax_ function==, which could produce an output like the following example:
[0.2, 0.3, 0.5]
The elements in the vector represent the probabilities for classes 0, 1, and 2 respectively; so in this case, the class with the highest probability is **2**.
In most scenarios that involve a known set of multiple classes, multiclass classification is used to predict mutually exclusive labels. For example, a penguin can't be both a _Gentoo_ and an _Adelie_. However, there are also some algorithms that you can use to train _multilabel_ classification models, in which there may be more than one valid label for a single observation. For example, a movie could potentially be categorized as both _science fiction_ and _comedy_.
## Evaluation Metrics
These metrics are often used to evaluate a model by plotting a _received operator characteristic_ (ROC) curve that compares the TPR and FPR for every possible threshold value between 0.0 and 1.0:
### Accuracy
The simplest metric you can calculate from the confusion matrix is _accuracy_ - the proportion of predictions that the model got right.
$$Accuracy = \frac{TN+TP}{TN+FN+TP+FP}$$
Accuracy might initially seem like a good metric to evaluate a model, but consider this. ==Suppose 11% of the population has diabetes. You could create a model that always predicts **0**, and it would achieve an accuracy of 89%, even though it makes no real attempt to differentiate between patients by evaluating their features==.
### Recall (True Positive Rate {TPR})
_Recall_ is a metric that measures the proportion of positive cases that the model identified correctly.
$$Recall = \frac{TP}{TP+FN}$$
### Precision
_Precision_ is a similar metric to recall, but measures the proportion of predicted positive cases where the true label is actually positive. In other words, what proportion of the patients _predicted_ by the model to have diabetes actually _have_ diabetes?
$$Precision = \frac{TP}{TP+FP}$$
### F1-Score
_F1-score_ is an overall metric that combines recall and precision. The formula for F1-score is:
$$F_1 = 2\times \frac{Precision \times Recall}{Precision + Recall}$$
### Area Under the Curve (AUC or False Positive Rate {FPR})
$$AUC = \frac{FP}{FP+TN}$$[Please read AUC and ROC from here!](https://learn.microsoft.com/en-us/training/modules/fundamentals-machine-learning/5-binary-classification?pivots=text)
