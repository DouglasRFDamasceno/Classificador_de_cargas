from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    production = models.IntegerField()
    consumption = models.CharField(max_length=200, default='0')
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.name
