# Generated by Django 4.1.2 on 2022-10-16 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_infectionperoid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InfectionPeroid',
            new_name='InfectionRecord',
        ),
    ]