# Generated by Django 3.2.15 on 2022-09-01 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0012_alter_house_dono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='descricao',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='house',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='house',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='house',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='house',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
