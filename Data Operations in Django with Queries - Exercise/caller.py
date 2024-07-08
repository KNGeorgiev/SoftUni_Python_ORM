import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Pet, Artifact, Location, Car


# def create_pet(name: str, species: str):
#     pet = Pet(
#         name = name,
#         species = species
#     )
#     pet.save()

#     return f"{pet.name} is a very cute {pet.species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


# def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
#     artifact = Artifact(
#         name = name,
#         origin = origin,
#         age = age,
#         description = description,
#         is_magical = is_magical
#     )
#     artifact.save()

#     return f"The artifact {artifact.name} is {artifact.age} years old!"


# def rename_artifact(artifact: Artifact, new_name: str):
    
#     if artifact.is_magical and artifact.age > 250:
#         artifact.name = new_name
#     artifact.save()


# def delete_all_artifacts():
#     Artifact.objects.all().delete()

# delete_all_artifacts()
# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)


# def show_all_locations():
#     locations = Location.objects.all().order_by('-id')
#     result = ''

#     for l in locations:
#         result += f'{l.name} has a population of {l.population}!\n'
#     return result
    

# def new_capital():
#     data = Location.objects.first()
#     if data:
#         data.is_capital = True
#         data.save()


# def get_capitals():
#     capitals = Location.objects.filter(is_capital=True).values('name')
#     return capitals


# def delete_first_location():
#     Location.objects.first().delete()


# print(show_all_locations())
# print(new_capital())
# print(get_capitals())


def apply_discount():
    all_cars = Car.objects.all()

    for car in all_cars:
        year_sum = sum([int(x) for x in str(car.year)])
        car.price_with_discount = car.price - car.price * year_sum / 100
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


apply_discount()
print(get_recent_cars())
