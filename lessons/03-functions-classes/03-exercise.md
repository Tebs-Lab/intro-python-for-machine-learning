# Exercise: Using Functions and Classes

This exercise is meant to help you practice:

* Creating and calling functions.
* Creating classes, instantiating objects, and using those objects.

# The Exercise

You will be writing a python script that creates functions and classes, then uses those functions and classes.

> Hint: some of Python's built in functions may help you write this code faster. See: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

## Part 1: Standalone Functions

Many functions are useful entirely on their own, and don't need to be part of a class. To practice creating and using standalone functions write the following two functions. Make sure to test each one by creating input and checking that it's output is what you expect.

### Mean

Create a function called mean that accepts a list of numbers and returns the mean of those numbers. Remember, the mean is the sum of the values divided by the number of values. 

You should be able to use your function like this:

```python
numbers = [5, 10, 15]
m = mean(numbers)
print(m) # 10
```

**Be sure to test your code with more than just this single test case!**

> Hint: consider using the `sum` and `len` built in functions...

### Median

Create a function called median that accepts a list of numbers and returns the median of those numbers. Remember, the median is the value at the center of the sorted dataset. If there are an even number of values in the dataset the median is the mean of the two center values.

You should be able to use your function like this:

```python
numbers = [5, 10, 15]
m = mean(numbers)
print(m) # 10
```

**Be sure to test your code with more than just this single test case!**

> Hint: Consider using the `sorted` built in function.
> Hint: You can determine if a list has an even number of items with `is_even = len(numbers) % 2 == 0`. See: [The modulo operator](https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/)

## Part 2: Classes

Now we're going to take the two functions you created and turn them into a class! Consider this incomplete class stub:

```python
class Averages:
    def __init__(self, input_data):
        pass # replace with your code

    def mean(self):
        pass # replace with your code

    def median(self):
        pass # replace with your code
```

Create a new python file and, using the code you wrote in part one, complete this class stub such that:

* When you create a new instance of the `Averages` class the input_data is copied and stored on `self.data`. Hint, there are [several ways to make a copy](https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list). 
* When a user calls the mean and median methods, the appropriate value is returned. You may reuse your code from part 1.

Example use, when your class is complete you should be able to use it as follows:

```python
avgs = Averages([5,10,15])
print(avgs.mean())) # 10
print(avgs.median()) # 10
```