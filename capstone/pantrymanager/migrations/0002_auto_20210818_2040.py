# Generated by Django 3.1.8 on 2021-08-19 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantrymanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantry',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pantry',
            name='expiration',
            field=models.DateField(null=True),
        ),
    ]