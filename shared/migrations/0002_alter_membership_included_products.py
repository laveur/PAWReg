# Generated by Django 4.1.3 on 2023-03-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='included_products',
            field=models.ManyToManyField(blank=True, to='shared.product'),
        ),
    ]
