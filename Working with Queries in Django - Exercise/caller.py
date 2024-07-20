import os
from typing import List
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal
from django.db.models import Case, When, Value, Q

###########################################################################

# def show_highest_rated_art():
#     highest = ArtworkGallery.objects.order_by('-rating', 'id').first()
#     return f"{highest.art_name} is the highest-rated art with a {highest.rating} rating!"


# def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
#     ArtworkGallery.objects.bulk_create([first_art, second_art])


# def delete_negative_rated_arts():
#     ArtworkGallery.objects.filter(rating__lt=0).delete()


# artwork1 = ArtworkGallery(artist_name='Vincent van Gogh', art_name='Starry Night', rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name='Leonardo da Vinci', art_name='Mona Lisa', rating=5, price=1500000.0)

# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())

###########################################################################

# def show_the_most_expensive_laptop():
#     most_expensive = Laptop.objects.order_by('-price', '-id').first()
#     return f"{most_expensive.brand} is the most expensive laptop available for {most_expensive.price}$!"

# def bulk_create_laptops(*args):
#     Laptop.objects.bulk_create(*args)


# def update_to_512_GB_storage():
#    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


# def update_to_16_GB_memory():
#     Laptop.objects.filter(brand__in=['Apple', 'Dell', 'Acer']).update(memory=16)


# def update_operation_systems():
#     Laptop.objects.update(
#         operation_system=Case(
#             When(brand='Asus', then=Value('Windows')),
#             When(brand='Apple', then=Value('MacOS')),
#             When(brand='Dell', then=Value('Linux')),
#             When(brand='Acer',then=Value('Linux')),
#             When(brand='Lenovo', then=Value('Chrome OS'))
#         )
#     )


# def delete_inexpensive_laptops():
#     Laptop.objects.filter(price__lt=1200).delete()

###########################################################################

# def bulk_create_chess_players(*args):
#     ChessPlayer.objects.bulk_create(*args)


# def delete_chess_players():
#     ChessPlayer.objects.filter(title="no title").delete()


# def change_chess_games_won():
#     ChessPlayer.objects.filter(title="GM").update(games_won=30)


# def change_chess_games_lost():
#     ChessPlayer.objects.filter(title="no title").update(games_lost=25)


# def change_chess_games_drawn():
#     ChessPlayer.objects.all().update(games_drawn=10)


# def grand_chess_title_GM():
#     ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


# def grand_chess_title_IM():
#     ChessPlayer.objects.filter(Q(rating__gte=2300) & Q(rating__lt=2400)).update(title="IM")


# def grand_chess_title_FM():
#     ChessPlayer.objects.filter(Q(rating__gte=2200) & Q(rating__lt=2300)).update(title="FM")


# def grand_chess_title_regular_player():
#     ChessPlayer.objects.filter(rating__lt=2200).update(title="regular player")

# player1 = ChessPlayer(
#     username='Player1',
#     title='no title',
#     rating=2200,
#     games_played=50,
#     games_won=20,
#     games_lost=25,
#     games_drawn=5,
# )
# player2 = ChessPlayer(
#     username='Player2',
#     title='IM',
#     rating=2350,
#     games_played=80,
#     games_won=40,
#     games_lost=25,
#     games_drawn=15,
# )

# # Call the bulk_create_chess_players function
# bulk_create_chess_players([player1, player2])

# # Call the delete_chess_players function
# delete_chess_players()

# # Check that the players are deleted
# print("Number of Chess Players after deletion:", ChessPlayer.objects.count())

###########################################################################

def set_new_chefs():
    Meal.objects.update(
        chef=Case(
            When(meal_type="Breakfast", then=Value("Gordon Ramsay")),
            When(meal_type="Lunch", then=Value("Julia Child")),
            When(meal_type="Dinner", then=Value("Jamie Oliver")),
            When(meal_type="Snack", then=Value("Thomas Keller"))
        )
    )


def set_new_preparation_times():
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type="Breakfast", then=Value("10 minutes")),
            When(meal_type="Lunch", then=Value("12 minutes")),
            When(meal_type="Dinner", then=Value("15 minutes")),
            When(meal_type="Snack", then=Value("5 minutes"))
        )
    )


def update_low_calorie_meals():
    Meal.objects.filter(Q(meal_type="Breakfast") | Q(meal_type="Dinner")).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(Q(meal_type="Lunch") | Q(meal_type="Snack")).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(Q(meal_type="Lunch") | Q(meal_type="Snack")).delete()


# meal1 = Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
# )

# meal2 = Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
# )
# # Test the set_new_chefs function
# set_new_chefs()

# # Test the set_new_preparation_times function
# set_new_preparation_times()

# # Refreshes the instances 
# meal1.refresh_from_db()
# meal2.refresh_from_db()

# # Print the updated meal information
# print("Meal 1 Chef:", meal1.chef)
# print("Meal 1 Preparation Time:", meal1.preparation_time)
# print("Meal 2 Chef:", meal2.chef)
# print("Meal 2 Preparation Time:", meal2.preparation_time)
