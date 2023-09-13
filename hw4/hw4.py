import random
import statistics as st

range_ = 100


def generate_hundred_random_numbers():
    return [random.randrange(1, range_) for i in range(range_)]


print([st.median(generate_hundred_random_numbers()) for i in range(range_)])
print([sum(generate_hundred_random_numbers()) for j in range(range_)])
