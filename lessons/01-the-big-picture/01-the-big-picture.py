"""
This script is an example of the kind of code you should be able to 
read and write by the end of this class. It is a fairly simple example
of executing a machine learning task using open source libraries.

The purpose of this resource is to give students a good idea of where
we are headed in this class, but it's okay (expected in fact) if you
don't fully understand how/why this code works the first time you see it.

Over the course of the class we'll peel back all the layers of this onion,
and return to this example as a touchstone. As we learn more about the 
fundamentals of Python, this code will become easier to understand, modify,
and recreate yourself.

In this code we will:

    * Import the libraries we need.
    * Load a dataset from a csv file.
    * Preprocess that data slightly to be used by our ML algorithm.
    * Build and train a simple ML Model.
    * Show the results.

Note: as a learning resource this code contains a LOT more comments
than you should expect to find in production code, and more than you 
should expect to put in your own code.
"""

# pandas is a tool for loading and manipulating data.
# It's kind of like a really fancy spreadsheet inside your 
# Python code...
import pandas as pd

# sklearn is an open source machine learning library.
# It provides high quality implementations of ML algorithms.
# Docs for this particular one: 
#    https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
from sklearn.neighbors import KNeighborsClassifier

# Sklearn also provides tools for creating training/validation/test data
#    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
from sklearn.model_selection import train_test_split

# Our data is in a CSV file, and pandas has a built in function for
# reading that kind of data: 
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

# We're using a "relative file path" to load data that is bundled with this
# repository
heart_dataset = pd.read_csv('../../datasets/uci-heart-disease/heart.csv')

# These functions produce information about the loaded dataset.
# The print function (built into python) sends it to our terminal.

# Show us the first few rows of data
print(heart_dataset.head())
print() # Print a blank line...

# Print some descriptive statistics about each column
print(heart_dataset.describe())
print()

# Print the names and "types" of the columns
for col_name, data_type in zip(heart_dataset.columns, heart_dataset.dtypes):
    print(col_name, data_type)
print()

# Before we can do a supervised learning task, we need to 
# break the data into two parts, the input and the label.
# in our case the label is "did this person have heart disease or not"
# and the data is all the measurements included in the data.

# Get just the target, heart disease or not
labels = heart_dataset['target']

# Remove the target from the data
input_data = heart_dataset.drop(columns=['target'])

# Now we're going to create training and test data
# by sampling from our dataset using an sklearn utility.
training_data, test_data, training_labels, test_labels = train_test_split(
    input_data, 
    labels, 
    test_size=0.20
)

# Now we're going to make a KNN model using sklearn
# We're just going to use the "default" settings so 
# we don't have to supply any additional parameters
model = KNeighborsClassifier()

# All the sklearn models follow the pattern
# "Create -> fit -> use/predict"

# Fitting the model uses the training data and labels to 
# "learn" patterns in the data.
model.fit(training_data, training_labels)

# Now, we can score our model on the held out data!
print("Test accuracy: ", model.score(test_data, test_labels))