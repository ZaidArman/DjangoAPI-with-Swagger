from django.db import models

class Passenger(models.Model):
    passenger_id = models.IntegerField(unique=True)
    survived = models.BooleanField()
    pclass = models.IntegerField()
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    age = models.FloatField(null=True, blank=True)
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    ticket = models.CharField(max_length=100)
    fare = models.FloatField()
    cabin = models.CharField(max_length=50, null=True, blank=True)
    embarked = models.CharField(max_length=1)

    def __str__(self):
        return self.name
