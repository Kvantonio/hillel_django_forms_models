# Generated by Django 3.1.4 on 2021-01-04 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_myperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myperson',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]