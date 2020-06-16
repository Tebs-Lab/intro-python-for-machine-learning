# Classes are a form of complex data that combines data and functions.
# ML Libraries frequently provide classes as one of the main features, 
# where each model is a class that has an internal state as well as some
# useful functions for fitting/training the model and using it to make
# predictions.


# Classes are used throughout the programming industry, not just by ML
# folks.

class SimpleLinearRegression:
    """
    This simplistic implementation of linear regression assumes data is provided
    in a two dimensional space and creates a line of best fit using squared error.

    The resulting line is in the form y=mX+b where m is the slope of the regression
    line and b is the y-intercept of that line. We're using a classical formula for
    computing this line using covariance, but not explaining these concepts. For
    a more complete treatment of least squares regression see: 
       
       https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/regression-library/v/introduction-to-residuals-and-least-squares-regression

    NOTE: This code is meant as a tool to teach the conept of classes NOT as a tool for
    performing statistical analysis. Use Numpy, SciKit-Learn, or some other well
    tested library for your analytical needs.
    """

    # Note, all methods should take "self" as the first parameter.
    # This has to do with how Python implements classes. The first
    # passed parameter is always a reference to the current instance
    # of this class and the name is always "self" by convention.
    def __init__(self):
        """
        This method is called the "constructor" and in python it always uses 
        the special name __init__. Every time we create a new instance of this
        class this function will be called to initialize that new instance.
        
        We can pass parameters to this function if our class requires data at
        the time of its creation. Our example class does not need initialization
        data, so we don't pass any parameters to it.
        """

        # Within methods of the class, the keyword 'self' refers to the 
        # particular instance of the class — in this case it's the instance
        # that we are creating in the constructor.
        self.slope = None
        self.y_intercept = None
    

    def fit(self, x_points, y_points):
        """
        This method accepts two lists representing the points in the 
        dataset in the following format:
            x_points: [x1, x2, x3, ...]
            y_points: [y1, y2, y3, ...]

        Calling this method will result in the slope and y_intercept being set 
        after computing the line of best fit using the squared error for the provided
        data points.
        """
        # It's common to check that the input is valid, and raise an
        # exeption if the caller made a mistake.
        if len(x_points) != len(y_points):
            raise ValueError("There must be the same number of x and y data points.")

        x_mean = sum(x_points) / len(x_points)
        y_mean = sum(y_points) / len(y_points)

        x_variance = 0.0
        covariance = 0.0
        for x, y in zip(x_points, y_points):
            covariance += (x - x_mean) * (y - y_mean)
            x_variance += (x - x_mean)**2
        
        # Note: now we are setting the properties on self
        # that we created in the constructor
        self.slope = covariance / x_variance
        self.y_intercept = y_mean - (self.slope * x_mean)


    def predict(self, x):
        """
        Given an x value compute and return the corresponding y value
        from on the regression line.
        """
        return (self.slope * x) + self.y_intercept


# When we want to use a class, we envoke the constructor using the 
# name of the class.
linear_model = SimpleLinearRegression()

# We've created a unique data type!
print(type(linear_model)) # <class '__main__.SimpleLinearRegression'>

# We need some data to fit our linear model...
# Here is some very simple toy data that has
# perfect covariance to test our model...
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Calling a method is done using dot notation.
linear_model.fit(x_values, y_values)

# We can access the properties of an object this way too
print(linear_model.slope, linear_model.y_intercept) # 2, 0

# Using our predict method...
prediction = linear_model.predict(3.45)
print(prediction)

# Micro-exercise: Create a second instance of the SimpleLinearModel class
# then create two new lists of x and y data and fit the model on that data.
# Then, print the slope and y_intercept of your model, and use it to make a
# prediction for some made up x point.