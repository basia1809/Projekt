from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

# Models' names are in Polish, because of admin panel, which will be used by Pole

USLUGI = [
    ('rl', 'Renowacja lakieru'),
    ('ps', 'Pielęgnacja skór'),
    ('mp', 'Myjnia premium')
]

RODZAJE_SAMOCHODOW = [
    ('sed', 'Sedan'),
    ('kom', 'Kombi'),
    ('hat', 'Hatchback'),
    ('suv', 'SUV'),
    ('kab', 'Kabriolet')
]

class Post(models.Model):
    tytuł = models.CharField(max_length=200, null=False, blank=False)
    treść = models.TextField(null=False, blank=False)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.tytuł} - {self.data}'

class Zamowienie(models.Model):
    imię = models.CharField(max_length=200, null=False, blank=False)
    nazwisko = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefon = models.CharField(max_length=9, validators=[RegexValidator(r'^[0-9]{9}$','Numer musi zawierac 9 cyfr')], 
        null=False, blank=False)
    usługa = models.CharField(choices=USLUGI, max_length=100, null=False, blank=False)
    rodzaj_samochodu = models.CharField(choices=RODZAJE_SAMOCHODOW, max_length=100, null=False, blank=False)
    komentarz = models.TextField(null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.imię} {self.nazwisko} - {self.usługa} / {self.data.strftime("%Y-%m-%d %H:%M:%S")}'