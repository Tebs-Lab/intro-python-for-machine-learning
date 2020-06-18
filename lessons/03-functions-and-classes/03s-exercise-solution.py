## Part 1: Standalone Functions

### Mean

def mean(input_list):
    return sum(input_list) / len(input_list)

# Provided test, you should add more.
numbers = [5, 10, 15]
m = mean(numbers)
print(m) # 10

### Median

def median(input_list):
    n = len(input_list)
    sorted_list = sorted(input_list)

    # No elements, no median
    if n == 0:
        return None
    # Even case
    elif n % 2 == 0:
        a = sorted_list[n // 2]
        b = sorted_list[n // 2 - 1]
        return (a + b) / 2
    # Odd case
    else:
        return sorted_list[n // 2]

# Provided test, you should add more.
numbers = [5, 10, 15]
m = median(numbers)
print(m) # 10

# ## Part 2: Classes

class Averages:
    def __init__(self, input_data):
        self.data = input_data

    def mean(self):
        return sum(self.data) / len(self.data) # replace with your code

    def median(self):
        n = len(self.data)
        sorted_list = sorted(self.data)

        # No elements, no median
        if n == 0:
            return None
        # Even case
        elif n % 2 == 0:
            a = sorted_list[n // 2]
            b = sorted_list[n // 2 - 1]
            return (a + b) / 2
        # Odd case
        else:
            return sorted_list[n // 2]



# Sample tests, you should add more.
avgs = Averages([5,10,15])
print(avgs.mean()) # 10
print(avgs.median()) # 10
