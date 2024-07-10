import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character
from django.db.models import Q, F

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


# def get_deluxe_rooms():

#     all_deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
#     result = []
#     for room in all_deluxe_rooms:
#         if room.id % 2 == 0:
#             result.append(str(room))

#     return "\n".join(result)


# def increase_room_capacity():
#     rooms = HotelRoom.objects.all().order_by('id')
#     previous_capacity = 0

#     for room in rooms:

#         if room.is_reserved:
#             if room.id == HotelRoom.objects.first().id:
#                 room.capacity += room.id
#             else:
#                 room.capacity += previous_capacity

#         previous_capacity = room.capacity
    
#     HotelRoom.objects.bulk_update(rooms, ['capacity'])


# def reserve_first_room():
#     room = HotelRoom.objects.first()
#     if not room.is_reserved:
#         room.is_reserved = True
#         room.save()


# def delete_last_room():
#     HotelRoom.objects.last().delete()


def update_characters():
    Character.objects.filter(class_name="Mage").update(
        level = F("level")+3,
        intelligence = F("intelligence")-7
    )

    Character.objects.filter(class_name="Warrior").update(
        level = F("hit_points")/2,
        intelligence = F("dexterity")+4
    )

    Character.objects.filter(Q(class_name="Assassin") | Q(class_name="Scout")).update(
        inventory = "The inventory is empty"
    )


def fuse_characters(first_character: Character, second_character: Character):
    
    fusion_name = first_character.name + " " + second_character.name
    fusion_class_name = "Fusion"
    fusion_level = (first_character.level + second_character.level) // 2
    fusion_strength = (first_character.strength + second_character.strength) * 1.2
    fusion_dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    fusion_intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    fusion_hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ['Mage', 'Scout']:
        fusion_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        fusion_inventory = "Dragon Scale Armor, Excalibur"
    
    Character.objects.create(
        name = fusion_name,
        class_name = fusion_class_name,
        level = fusion_level,
        strength = fusion_strength,
        dexterity = fusion_dexterity,
        intelligence = fusion_intelligence,
        hit_points = fusion_hit_points,
        inventory = fusion_inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()