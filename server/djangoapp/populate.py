from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
          "name": "NISSAN",
          "description": "Great cars. Japanese technology",
          "color": "Red"
        },
        {
          "name": "Mercedes",
          "description": "Great cars. German technology",
          "color": "Silver"
        },
        {
          "name": "Audi",
          "description": "Great cars. German technology",
          "color": "Blue"
        },
        {
          "name": "Kia",
          "description": "Great cars. Korean technology",
          "color": "Black"
        },
        {
          "name": "Toyota",
          "description": "Great cars. Japanese technology",
          "color": "White"
        },
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
          CarMake.objects.create(
            name=data['name'],
            description=data['description'],
            color=data['color']
          )
        )

    car_model_data = [
        {
          "name": "Pathfinder",
          "type": "SUV",
          "year": 2023,
          "price": "1000000",
          "car_make": car_make_instances[0]
        },
        {
          "name": "Qashqai",
          "type": "SUV",
          "year": 2023,
          "price": "2000000",
          "car_make": car_make_instances[0]
        },
        {
          "name": "XTRAIL",
          "type": "SUV",
          "year": 2023,
          "price": "1500000",
          "car_make": car_make_instances[0]
        },
        {
          "name": "A-Class",
          "type": "SUV",
          "year": 2023,
          "price": "4000000",
          "car_make": car_make_instances[1]
        },
        {
          "name": "C-Class",
          "type": "SUV",
          "year": 2023,
          "price": "3000000",
          "car_make": car_make_instances[1]
        },
        {
          "name": "E-Class",
          "type": "SUV",
          "year": 2023,
          "price": "4500000",
          "car_make": car_make_instances[1]
        },
        {
          "name": "A4",
          "type": "SUV",
          "year": 2023,
          "price": "500000",
          "car_make": car_make_instances[2]
        },
        {
          "name": "A5",
          "type": "SUV",
          "year": 2023,
          "price": "900000",
          "car_make": car_make_instances[2]
        },
        {
          "name": "A6",
          "type": "SUV",
          "year": 2023,
          "price": "1500000",
          "car_make": car_make_instances[2]
        },
        {
          "name": "Sorrento",
          "type": "SUV",
          "year": 2023,
          "price": "2500000",
          "car_make": car_make_instances[3]
        },
        {
          "name": "Carnival",
          "type": "SUV",
          "year": 2023,
          "price": "600000",
          "car_make": car_make_instances[3]
        },
        {
          "name": "Cerato",
          "type": "Sedan",
          "year": 2023,
          "price": "1000000",
          "car_make": car_make_instances[3]
        },
        {
          "name": "Corolla",
          "type": "Sedan",
          "year": 2023,
          "price": "700000",
          "car_make": car_make_instances[4]
        },
        {
          "name": "Camry",
          "type": "Sedan",
          "year": 2023,
          "price": "900000",
          "car_make": car_make_instances[4]
        },
        {
          "name": "Kluger",
          "type": "SUV",
          "year": 2023,
          "price": "4700000",
          "car_make": car_make_instances[4]
        },
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            price=data['price']
        )
