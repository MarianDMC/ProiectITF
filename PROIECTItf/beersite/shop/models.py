from django.db import models

# Create your models here.

CATEGORIES = [
    ("Belgian", "Belgian"),
    ("Dark Beer", "Dark Beer"),
    ("India Pale Ale", "India Pale Ale"),
    ("Pale Ale/Red Ale", "Pale Ale/Red Ale"),
    ("Pils/Lager/Weiss", "Pils/Lager/Weiss")
]


class BeerTypes(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=150, choices=CATEGORIES)
    price = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    alcohol_level = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    in_stock = models.BooleanField(default=True)
    image_cover = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'Bere: numele {self.name}, categoria {self.category}, pret {self.price}, cantitate {self.quantity},alcool {self.alcohol_level}, descriere {self.description}, disponibilitate {self.in_stock}'

    def __repr__(self):
        return self.__str__()
