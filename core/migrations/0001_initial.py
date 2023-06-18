# Generated by Django 4.2.2 on 2023-06-18 15:46

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytuł', models.CharField(max_length=200)),
                ('treść', models.TextField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imię', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^[0-9]{9}$', 'Numer musi zawierac 9 cyfr')])),
                ('usługa', models.CharField(choices=[('rl', 'Renowacja lakieru'), ('ps', 'Pielęgnacja skór'), ('mp', 'Myjnia premium')], max_length=100)),
                ('rodzaj_samochodu', models.CharField(choices=[('sed', 'Sedan'), ('kom', 'Kombi'), ('hat', 'Hatchback'), ('suv', 'SUV'), ('kab', 'Kabriolet')], max_length=100)),
                ('komentarz', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_usługi', models.DateField(blank=True, null=True)),
            ],
        ),
    ]