from django.db import models

# Create your models here.
class Komputer(models.Model):
    model = models.CharField(max_length=255)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    soni = models.IntegerField()
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)