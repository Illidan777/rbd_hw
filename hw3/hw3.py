n = int(input('Enter random natural number:'))


# Task1
def generate_squared_numbers(input_number):
    natural_numbers = list(range(1, input_number + 1))
    squared_numbers = []
    for i in natural_numbers:
        squared_numbers.append(i ** 2)
    return squared_numbers


print('Task 1 result: ', generate_squared_numbers(n))


# Task2
def square(item):
    return item ** 2


def generate_squared_numbers_with_map(input_number):
    natural_numbers = list(range(1, input_number + 1))
    return list(map(square, natural_numbers))


print('Task 2 result: ', generate_squared_numbers_with_map(n))


# Task3
def generate_squared_numbers_with_comprehensive_list(input_number):
    natural_numbers = list(range(1, input_number + 1))
    return [item ** 2 for item in natural_numbers]


print('Task 3 result: ', generate_squared_numbers_with_comprehensive_list(n))


# Task4
def get_squared_numbers(input_number):
    natural_numbers = list(range(1, input_number + 1))

    return [item for item in natural_numbers if natural_numbers.__contains__(item ** 0.5)]


print('Task 4 result: ', get_squared_numbers(n))

# Task5
start_interval = int(input('Enter start number of interval:'))
end_interval = int(input('Enter end number of interval:'))

if end_interval < start_interval or end_interval == start_interval:
    raise Exception('End of interval can not be less or equals to start!')


check_belong_to_interval = lambda number, interval_point_a, interval_point_b: interval_point_a <= number <= interval_point_b


print(f'Task 5 result. Does number {n} belongs to interval [{start_interval}, {end_interval}]? Result: ', check_belong_to_interval(n, start_interval, end_interval))

