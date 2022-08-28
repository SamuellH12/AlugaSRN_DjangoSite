# Generated by Django 3.2.15 on 2022-08-27 14:23

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_house_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='endereco',
            field=django_google_maps.fields.AddressField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
