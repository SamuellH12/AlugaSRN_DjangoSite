# Generated by Django 3.2.15 on 2022-09-01 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0011_alter_house_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='dono',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
