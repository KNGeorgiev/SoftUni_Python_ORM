from datetime import date
from django.db import models
from django.forms import ValidationError

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

class Mammal(Animal):
    fur_color = models.CharField(max_length=50)

class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)

class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True

class ZooKeeper(Employee):
    ANIMAL_TYPES = (
        ('Mammals', 'Mammals'),
        ('Birds', 'Birds'),
        ('Reptiles', 'Reptiles'),
        ('Others', 'Others')
    )
    specialty = models.CharField(max_length=10, choices=ANIMAL_TYPES)
    managed_animals = models.ManyToManyField(Animal)

    def clean(self):
        if self.specialty not in dict(self.ANIMAL_TYPES).keys():
            raise ValidationError("Specialty must be a valid choice.")
    

class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = ((True, 'Available'), (False, 'Not Available'))
        kwargs['default'] = True
        super().__init__(*args, **kwargs)

class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)
    availability = BooleanChoiceField()


class ZooDisplayAnimal(Animal):
    SPECIES_AT_RISK = ["Cross River Gorilla", "Orangutan", "Green Turtle"]

    class Meta:
        proxy = True

    def display_info(self):
        return f"Meet {self.name}! Species: {self.species}, born {self.birth_date}. It makes a noise like '{self.sound}'."
    
    def is_endangered(self):
        if self.species in self.SPECIES_AT_RISK:
            return f"{self.species} is at risk!"
        else:
            return f"{self.species} is not at risk."