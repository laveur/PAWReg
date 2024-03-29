# Generated by Django 4.1.3 on 2023-03-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='is_merchant',
            field=models.BooleanField(default=False, verbose_name='I am planning to be a Merchant'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Registration is paid'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='is_parent',
            field=models.BooleanField(default=False, verbose_name='I am bringing child'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='is_part_host',
            field=models.BooleanField(default=False, verbose_name='I am planning to host a party'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='is_volunteer',
            field=models.BooleanField(default=False, verbose_name='I want to volunteer'),
        ),
    ]
