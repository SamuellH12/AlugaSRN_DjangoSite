from django.conf import settings
from django.db import models
from django.utils import timezone


class House(models.Model):
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=14, decimal_places=2)
    descricao = models.TextField(max_length=2000)
    imagem = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    cidade = models.CharField(max_length=40, default="São Raimundo Nonato")
    bairro = models.CharField(max_length=40, default="Centro")

    def publish(self):
        self.published_date = timezone.now()
        self.save()