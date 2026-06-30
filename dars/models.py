from django.db import models

# Create your models here.
class Meva(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.IntegerField()
    haqida = models.TextField(blank=True, null=True)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
    sotilgan_vaqt = models.TimeField(null=True, blank=True)
    mavjudmi = models.BooleanField(default=True)
    soni = models.FloatField()