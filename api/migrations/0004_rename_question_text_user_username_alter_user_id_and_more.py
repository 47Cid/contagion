# Generated by Django 4.1.2 on 2022-10-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_pub_date_user_creation_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='question_text',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='infection_probabilty',
            field=models.FloatField(default=0, max_length=200),
        ),
    ]
