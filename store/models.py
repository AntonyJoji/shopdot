from django.db import models

# Create your models here.
class productdata(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.CharField(max_length=300)
    fea=models.CharField(max_length=300)

def __str__(self):
    return str(self.id)+":"+self.name