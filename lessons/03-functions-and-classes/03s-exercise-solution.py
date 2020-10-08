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
        return sorted_list[n // 2] # Note: Integer division is needed for odd n

# Provided test, you should add more.
numbers = [5, 10, 15]
m = median(numbers)
print(m) # 10

# ## Part 2: Classes

class Averages:
    def __init__(self, input_data):
        self.data = input_data.copy()

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
            return sorted_list[n // 2] # Note: Integer division is needed for odd n



# Sample tests, you should add more.
l_one = [5,10,15]
avgs = Averages(l_one)
print(avgs.mean()) # 10
print(avgs.median()) # 10

# Prove that we made a copy of the list, no side effects.
l_one.append(25)
print(avgs.mean()) # 10
print(avgs.median()) # 10
