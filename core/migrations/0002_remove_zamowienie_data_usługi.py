# Generated by Django 4.2.2 on 2023-06-18 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zamowienie',
            name='data_usługi',
        ),
    ]
