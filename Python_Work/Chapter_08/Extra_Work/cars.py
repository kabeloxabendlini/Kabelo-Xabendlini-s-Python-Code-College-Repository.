def make_car(manufacturer, model, **options):
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in options.items():
        car_info[key] = value
    return car_info

# Example call
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)