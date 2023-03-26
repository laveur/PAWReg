# Generated by Django 4.1.3 on 2023-03-26 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0006_producttype_user_selection_required'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Value')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.producttypeattribute')),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.membership')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.product')),
            ],
        ),
    ]