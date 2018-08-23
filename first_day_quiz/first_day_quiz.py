def hello_ta():
    # Your solution here
    pass

def pi():
    """
    Computes a rough estimate to the value of pi rounded to 5 decimals.
    Do NOT just return a static value, you must implement the equation
    provided on the wiki. You will not receive credit otherwise.
    >>> pi()
    3.19419
    """
    # Your solution here.
    pass

def hybrid(car_cost, miles_per_year, cost_of_gas_per_gallon, car_efficiency, car_5_year_resale_value):
    """
    Returns 2 items:
        - the total cost of fuel for 5 years if you bought this car
        - the total cost of owning the car for 5 years (fuel + depreciation in the car's value)

    Parameters:
        car_cost: the amount the car costs upon initial purchase
        miles_per_year: the amount of miles you expect to drive per year
        cost_of_gas_per_gallon: the cost of a gallon of gas
        car_efficiency: expected miles per gallon of the car
        car_5_year_resale_value: the expected value of the car after 5 years

    >>> hybrid(10000, 2000, 2.50, 45, 7500)
    (555.0, 3055.0)
    """
    # Your solution here.
    pass

def montehall(num_iterations=1000):
    """
    Runs the Monty Hall simulation num_iterations times.

    Returns 2 values:
        - a counter which keeps track of if you do switch doors and win.
        - a counter which keeps track of if you don't switch doors and win.

    >>> switch, no_switch = montehall()
    >>> switch + no_switch = 1000
    >>> switch > no_switch
    >>> switch, no_switch = montehall(200)
    >>> switch + no_switch = 200
    >>> switch > no_switch
    """
    # Your solution here.
    pass

def hotplate(matrix):
    """
    Returns a 2D matrix in which the heat distribution has stabilized.
    We define stabilization as if no values in the matrix change by
     no more than 0.1.

    >>> matrix = [ [0.0, 100.0, 30.7],\
                   [10.5, 45.0, 50.3],\
                   [11.1, 33.5, 48.2]]
    >>> hotplate(matrix)
    [[55.25, 45.7, 75.15], [18.7, 48.575, 41.3], [22.0, 34.77, 41.9]]
    """
    # Your solution here.
    pass

def pig_latin(input):
    """
    Returns the input translated into pig latin.

    >>> pig_latin("i wrote this program because i can not speak pig latin")
    "iay otewray isthay ogrampray ecuasebay iay ancay otnay eakspay igpay atinlay"
    """
    # Your solution here
    pass

def unique_words(input):
    """
    Returns a mapping of unique words and the count
    of how often they appear in the input text.

    >>> input_text = "This is a sentence with some repeated words and some non-repeated words."
    >>> mapping = unique_words(input_text)
    >>> mapping['this']
    1
    >>> mapping['is']
    1
    >>> mapping['a']
    1
    >>> mapping['repeated']
    1
    >>> mapping['some']
    2
    >>> mapping['words']
    1
    """
    # Your solution here.
    pass
