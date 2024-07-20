import os
from typing import List
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import ArtworkGallery, Laptop, ChessPlayer
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

def bulk_create_chess_players(*args):
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM():
    ChessPlayer.objects.filter(Q(rating__gte=2300) & Q(rating__lt=2400)).update(title="IM")


def grand_chess_title_FM():
    ChessPlayer.objects.filter(Q(rating__gte=2200) & Q(rating__lt=2300)).update(title="FM")


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__lt=2200).update(title="regular player")