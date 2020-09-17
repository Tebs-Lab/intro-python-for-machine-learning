# Exercise: Explore Decision Trees and Random Forests With Hyperparameter Search

This exercise is meant to help you practice:

* Building decision trees with `sklearn`
* Building random forests with `sklearn`
* Applying hyper-parameter search with `sklearn`

# The Exercise

In this exercise you'll build several different machine learning models using `sklearn` and evaluate their performance using the UCI Heart Disease dataset (provided in this repo). Unlike the previous exercise, you'll be using hyperparemeter search tools to automatically build, train, and evaluate several different versions of each model type. 

## Part 1: Decision Trees With Grid Search

Look at the sklearn [DecisionTreeClassifier documentation](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html). For each hyperparameter:

* Decide if it will impact the results or exclusively impact the computational speed.
* Pick at least 3 values for each hyperparameter that you'd like to include in your grid search.
    * If there are fewer than 3 valid choices, include all valid choices.
    * Carefully consider the choices, try to predict the impact of this hyperparameter on the outcome. 
    * Does this hyperparameter interact with others? 

Now that you've examined the hyperparemters and made your list, use sklearn's [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) to train and evaluate a DecisionTreeClassifier across all of your chosen hyperparameters.

* Identify the 3 best performing hyperparameter combinations.
* Identify the 3 worst performing hyperparameter combinations.
* Are there any interesting discernible patterns?

**Bonus challenges**

* Get the best performing model (look at the `best_estimator` property in the `GridSearchCV` documentation) and examine the `feature_importances_` of that `DecisionTree`. What are these, and what are they telling us?

* Create another `GridSearchCV` but this time include more metrics to score the model.
    * List of all built in metrics can be [found here](https://scikit-learn.org/stable/modules/classes.html#classification-metrics). I suggest using accuracy, precision, and recall.
    * A demo of using multiple metrics can be [found here](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#sphx-glr-auto-examples-model-selection-plot-multi-metric-evaluation-py)
    * If you were building a real world medical screening system, how would you decide to value and balance these different metrics?
        * [Read more about precision and recall](https://deepai.org/machine-learning-glossary-and-terms/precision-and-recall)
        * Double bonus: can you make your GridSearch compute specificity as well? [Hint](https://stackoverflow.com/questions/47704133/how-to-define-specificity-as-a-callable-scorer-for-model-evaluation)


## Part 2: Random Forests

Repeat all the steps of part 1 but using a [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html). The same bonus challenges apply.

## Part 3: Comparing Results

Write a few paragraphs summarizing the differences you've found with this dataset and these two types of model. While writing, consider the following:

* Is one of these two model types better "on average"?
* Consider the best and worse performing models of each type:
    * Are the worst performing models similarly bad, or is one much better?
    * What about the best performing, are they similarly good or is one much better?
* Compare the training times for each type.
    * Was one much faster than the other?
    * Which hyperparameters could a major impact on time to train?
    * Imagine your dataset became much larger, could the time-to-train become a serious problem?

**Bonus challenge**

* Compute and compare the 'feature importances' for each of your best performing models (the best performing DT and best performing RF).
    * Did both models consider the same features to be "most important"?
    * What about "least important"?
