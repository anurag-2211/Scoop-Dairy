# Generated by Django 4.2.7 on 2024-01-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice-Creams')], max_length=2),
        ),
    ]
