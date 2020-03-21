from django.db import models

# Create your models here.
class Position(models.Model):

    positionName = models.CharField(max_length=30)

    def __str__(self):
        return self.positionName

class Employee(models.Model):

    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Position = models.ForeignKey(Position, on_delete=models.CASCADE)