# Generated by Django 3.0.4 on 2020-06-07 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b', '0002_client_chiffre_affaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='chiffre_affaire',
        ),
    ]
