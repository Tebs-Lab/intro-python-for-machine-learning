# Exercise: Exploring Data With Jupyter, Pandas, and Matplotlib

This exercise is meant to help you practice:

* Reading documentation and using unfamiliar libraries.
* Writing and executing code in Jupyter Notebooks.
* Working with the `sklearn` library.
* Using creating test/train/validation splits and using them to evaluate models.

# The Exercise

In this exercise you'll build several different machine learning models using `sklearn` and evaluate their performance using the UCI Breast Cancer dataset (provided in this repo).

## Part One: Split your data

Import your data and split it into just two buckets, training and validation data. The dataset is small and we won't actually be publishing any of this research, we jut want to explore different models and how they generalize to held out data so we don't need a full on "test set" for this exercise.

Make sure to split the data into input and labels before performing the test/train split. 

**Bonus Challenges**: 

* Look into k-fold cross validation and use it to evaluate your model instead of a deterministic validation split [https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html)
* Perform an exploratory data analysis on the UCI data:
    * Is there any reason, based on your analysis, to remove some fields or perform any feature engineering?
    * Are there any interesting features that stand out?
    * Are there common outliers?
    * Visualize the distributions of the features, is there anything interesting?
    * Do any features clearly correlate more than others with malignancy?

## Part Two: Explore KNN

Build at least 6 different versions of the KNN model using different hyperparameters and evaluate their performance on the validation data. 

Before you evaluate their performance, form a hypothesis about which models you think will perform best and why. One you've evaluated the models, revisit your hypothesis: Was your intuition right? What surprised you? Can you explain your results?

> Hint: Look at the documentation for Sklearn's KNNClassifier for a list of hyperparamters and their possible values [https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).

**Bonus Challenge:** Use "Grid Search" to find the best hyperparameter combination [https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

## Part Three: Explore a Different Classifier

Pick another one of SKLearn's provided classifiers and similarly create at least 6 different versions of that model using different hyperparameters.

Hint, look at these two sklearn resources to find a lists of possible models to use:

* [https://scikit-learn.org/stable/supervised_learning.html](https://scikit-learn.org/stable/supervised_learning.html)
* [https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)

Before you create your models, find an article about this type of model, and read it!

> Hint: linear regression and decision trees are fairly straightforward, so if you're feeling overwhelmed they might be a good choice.

Similar to part two: Before you evaluate their performance, form a hypothesis about which models you think will perform best and why. One you've evaluated the models, revisit your hypothesis: Was your intuition right? What surprised you? Can you explain your results?

**Bonus Challenge:** Compare your best results with this model to your best results with KNN. Which one is better? Can you form a hypothesis about why one might outperform the other? Is there a way to test or evaluate your hypothesis?