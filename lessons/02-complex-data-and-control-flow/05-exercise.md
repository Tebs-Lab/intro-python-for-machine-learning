# Exercise: Using Complex Data and Control Flow

This exercise is meant to help you practice:

* Creating and modifying data in lists and dictionaries.
* Using loops.
* Using if statements.

# The Exercise

You will be writing scripts that utilizes lists, dictionaries, loops, and if statements. As you are writing the code, periodically execute the code in your terminal and print your variables to check your work and see their values.

## Part 1: Lists, Loops, and aggregating

* Create a list with 5 numbers in it and assign it to a variable.
* Create a variable called `list_sum` and assign it the value `0`
* Using a for loop, the `list_sum` variable and the `+=` operator, compute the sum of the values in your list.
* Using the `len` function, `list_sum`, and the `/` operator, compute the average of the values in your list and store it into a variable.
* Using another loop and an if statement inside the loop print all the values in your list that are less than the average.

## Part 2: Nested Data

Often times data is provided in strange, and sometimes deeply nested formats. Lists inside of lists, lists inside of dictionaries, dictionaries inside of dictionaries... and so on. Examining and understanding this kind of data is a skill programmers have to use frequently... Lets practice. Copy this python code into a new script:

```python
dictionary_challenge = {
    'key': 'value',
    'hello': 'world',
    'target': [
        {
            'this_is': 'getting',
            'sort': 'of',
            'tricky': ['Hello Earth', 'Hello Detroit', 'Hello World!']
        },
        {
            'too': 'far'
        }
    ]
}
```

* Using bracket notation to select each of the follow values from the above data structure and then print them to check your work:
    * `'world'`
    * `'far'`
    * `'Hello World!'`

* Now, instead of simply printing the values, modify them!
    * Replace `'world'` with `'friends'`
    * Replace `'far'` with `'cool'`
    * Replace `'Hello World!'` with `'So long and thanks for all the fish'`
    * Then, print the entire data structure to check your work.

Pro-tip, use the following code to "pretty print" the dictionary instead of the standard print:

```
from pprint import pprint
pprint(dictionary_challenge)
```