# Generated by Django 4.1.2 on 2022-10-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_travelrecord_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelrecord',
            name='arrived_at',
            field=models.DateTimeField(default=None, verbose_name='arrival time'),
        ),
        migrations.AddField(
            model_name='travelrecord',
            name='departed_at',
            field=models.DateTimeField(default=None, verbose_name='departure time'),
        ),
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(verbose_name='added on'),
        ),
        migrations.AlterField(
            model_name='user',
            name='infection_probability',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]
