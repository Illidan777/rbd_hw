import time


class Car:
    name = None
    age = None
    is_rnd = None

    def __init__(self, name, age, is_rnd):
        self.age = age
        self.name = name
        self.is_rnd = is_rnd

    def get_data(self):
        return self.name + ' ' + str(self.age) + ' ' + str(self.is_rnd)


class Toyota(Car):
    gear_force = 0

    def __init__(self, name, age, is_rnd, gear_force):
        super(Toyota, self).__init__(name, age, is_rnd)
        self.gear_force = gear_force

    def get_data(self):
        return super().get_data() + ' ' + str(self.gear_force)


car = Car('testcar', 12, True)
print(car.get_data())

toyota = Toyota('toyota', 12, False, 14)
print(toyota.get_data())


def uppercase_decorator(function):
    def wrapper(*args, **kwargs):
        func_result = function(*args, **kwargs)
        make_uppercase = func_result.upper()
        return make_uppercase

    return wrapper


def benchmark(function):
    def _benchmark(*args, **kwargs):
        current_time = time.process_time()
        res = function(*args, **kwargs)
        dt = time.process_time() - current_time
        print('Function processing time', dt)
        return res
    return _benchmark


def say_hi(name):
    return f'Hello, {name}'


decorate = uppercase_decorator(say_hi)
name = 'Alicdfgse'
print(decorate(name))

 
@benchmark
@uppercase_decorator
def say_hiNew(name):
    return f'Hello, {name}'


print(say_hiNew('dd'))

print(dir(car))


