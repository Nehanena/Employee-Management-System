from django.db import models

# Create your models here.
class Reg_tbl(models.Model):
    name = models.CharField(max_length=25)
    number = models.IntegerField()
    email = models.EmailField()
    passw = models.CharField(max_length=25)
