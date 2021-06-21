from django.db import models

# Create your models here.
class Book(models.Model):
	name=models.CharField(max_length=100)
	profile=models.ImageField()
	summary=models.CharField(max_length=2000)
	price=models.IntegerField()



