from django.conf import settings
from django.db import models
from django.utils import timezone
from django_google_maps import fields as map_fields


class House(models.Model):
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=14, decimal_places=2)
    descricao = models.TextField(max_length=2000)
    imagem = models.ImageField(upload_to='images/')
    endereco = map_fields.AddressField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo