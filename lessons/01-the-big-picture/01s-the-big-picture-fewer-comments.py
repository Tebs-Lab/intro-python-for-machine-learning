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

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load the data
heart_dataset = pd.read_csv('../../datasets/uci-heart-disease/heart.csv')

# Print basic info about the data
print(heart_dataset.head())
print() 

print(heart_dataset.describe())
print()

for col_name, data_type in zip(heart_dataset.columns, heart_dataset.dtypes):
    print(col_name, data_type)
print()

# Split the data into input and labels
labels = heart_dataset['target']
input_data = heart_dataset.drop(columns=['target'])

# Split the data into training and test
training_data, test_data, training_labels, test_labels = train_test_split(
    input_data, 
    labels, 
    test_size=0.20
)

# Build the model
model = KNeighborsClassifier()
model.fit(training_data, training_labels)

# See how it did.
print("Test accuracy: ", model.score(test_data, test_labels))