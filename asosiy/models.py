from django.db import models

# Create your models here.
class Kundalik(models.Model):
    vaqti=models.DateTimeField()
    izoh=models.TextField()
    maqsad=models.CharField(max_length=60)