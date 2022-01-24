import itertools
import math
import random
import re
import statistics
from collections import defaultdict

sampl_dict = defaultdict(list)

a, b = 3, 5  # sample comment


def add5(var):

    return var + 5


def test_add5():
    assert add5(4) == 9


c = a + b + 2
print("completed")
