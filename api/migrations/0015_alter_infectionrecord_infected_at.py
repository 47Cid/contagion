# Generated by Django 4.1.2 on 2022-10-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_rename_infected_from_infectionrecord_infected_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infectionrecord',
            name='infected_at',
            field=models.DateTimeField(default=None, verbose_name='infected at'),
        ),
    ]
