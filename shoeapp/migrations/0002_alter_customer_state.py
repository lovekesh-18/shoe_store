# Generated by Django 4.1.7 on 2023-03-26 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Rajasthan', 'Rajasthan'), ('Jammu', 'Jammu'), ('Pune', 'Pune'), ('Chennai', 'Chennai'), ('Haryana', 'Haryana'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi')], max_length=100),
        ),
    ]
