import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


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


# def apply_discount():
#     all_cars = Car.objects.all()

#     for car in all_cars:
#         year_sum = sum([int(x) for x in str(car.year)])
#         car.price_with_discount = car.price - car.price * year_sum / 100
#         car.save()


# def get_recent_cars():
#     return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


# def delete_last_car():
#     Car.objects.last().delete()


# apply_discount()
# print(get_recent_cars())


# def show_unfinished_tasks():
#     all_tasks = Task.objects.filter(is_finished=False)
#     result = ''

#     for task in all_tasks:
#         result += f'Task - {task.title} needs to be done until {task.due_date}!\n'
    
#     return result


# def complete_odd_tasks():
#     all_tasks = Task.objects.all()

#     for task in all_tasks:
#         if task.id % 2 != 0:
#             task.is_finished = True
#             task.save()


# def encode_and_replace(text: str, task_title: str):
#     decoded_text = ''.join(chr(ord(x) - 3) for x in text)
#     Task.objects.filter(title=task_title).update(description=decoded_text)


# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title='Simple Task').description)


def get_deluxe_rooms():

    all_deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    result = []
    for room in all_deluxe_rooms:
        if room.id % 2 == 0:
            result.append(str(room))

    return "\n".join(result)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')
    previous_capacity = 0

    for room in rooms:

        if room.is_reserved:
            if room.id == HotelRoom.objects.first().id:
                room.capacity += room.id
            else:
                room.capacity += previous_capacity

        previous_capacity = room.capacity
    
    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room():
    room = HotelRoom.objects.first()
    if not room.is_reserved:
        room.is_reserved = True
        room.save()


def delete_last_room():
    HotelRoom.objects.last().delete()