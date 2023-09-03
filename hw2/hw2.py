def service_alert_decorator(drive_function):
    def _service_alert_decorator(*args, **kwargs):
        res = drive_function(*args, **kwargs)

        limit_service_required_mileage = 10000
        if res < limit_service_required_mileage:
            print('No service required!')
        else:
            quotient = res // limit_service_required_mileage
            for _ in range(quotient):  # Loop 10 times
                print('Service required!')

    return _service_alert_decorator


class Vehicle:
    vehicle_type = None
    max_speed = None
    mileage = None
    passenger_capacity = None

    def __init__(self, vehicle_type, max_speed, mileage, passenger_capacity):
        self.vehicle_type = vehicle_type
        self.max_speed = max_speed
        self.mileage = mileage
        self.passenger_capacity = passenger_capacity

    def get_description(self):
        print(
            f'Vehicle type: {self.vehicle_type}. Max speed: {self.max_speed}. Mileage: {self.mileage}. Passenger capacity: {self.passenger_capacity}')

    def get_rent_price(self):
        return pow(self.passenger_capacity, 2)

    @service_alert_decorator
    def drive(self, mile_count):
        self.mileage += mile_count
        print(f'Vehicle has driven {mile_count} miles. Mileage was increased')
        return self.mileage


class Bus(Vehicle):
    def __init__(self, vehicle_type, max_speed, mileage):
        super().__init__(vehicle_type, max_speed, mileage, 50)

    def get_rent_price(self):
        percent = 10
        return self.passenger_capacity * (1 + (percent / 100))


class Auto(Vehicle):
    color = None

    def __init__(self, vehicle_type, max_speed, mileage, passenger_capacity):
        super().__init__(vehicle_type, max_speed, mileage, passenger_capacity)
        self.color = 'White'

    def get_description(self):
        print(
            f'Vehicle type: {self.vehicle_type}. Max speed: {self.max_speed}. Mileage: {self.mileage}.'
            f' Passenger capacity: {self.passenger_capacity}. Color: {self.color}')


vehicle = Vehicle('Moto', 250, 3000, 1)
print(vehicle.get_rent_price())
vehicle.get_description()
vehicle.drive(500)
vehicle.get_description()

auto1 = Auto('Auto', 110, 2000, 2)
auto2 = Auto('Auto', 230, 9300, 5)

print(auto1.get_rent_price())
auto1.get_description()
auto1.drive(999)
auto1.get_description()

print(auto2.get_rent_price())
auto2.get_description()
auto2.drive(700)
auto2.get_description()

bus1 = Bus('Bus', 60, 10000)
bus2 = Bus('Bus', 90, 20000)

print(bus1.get_rent_price())
bus1.get_description()
bus1.drive(10000)
bus1.get_description()

print(bus2.get_rent_price())
bus2.get_description()
bus2.drive(20)
bus2.get_description()
