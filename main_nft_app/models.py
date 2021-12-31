from django.db import models

# Create your models here.

class Project(models.Model): 
    media = models.CharField(max_length=250)
    name = models.CharField(max_length=200)
    external_link = models.URLField(max_length=350)
    description = models.TextField()
    collection = models.CharField(max_length=200)
    supply = models.IntegerField(default=0)
    chain = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'











