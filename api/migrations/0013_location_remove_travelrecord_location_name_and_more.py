# Generated by Django 4.1.2 on 2022-10-18 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_rename_infectionperoid_infectionrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('infection_factor', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='travelrecord',
            name='location_name',
        ),
        migrations.AddField(
            model_name='travelrecord',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.location'),
        ),
    ]
