# Generated by Django 3.2.15 on 2022-09-01 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0009_alter_house_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=14),
        ),
    ]