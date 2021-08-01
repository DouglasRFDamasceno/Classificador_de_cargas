from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    production = models.IntegerField()
    # def __str__(self):
    #     return self.name
