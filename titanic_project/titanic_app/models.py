from django.db import models

class Passenger(models.Model):
    # Choices for gender field
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    
    passenger_id = models.IntegerField(unique=True)
    survived = models.BooleanField()
    pclass = models.IntegerField()
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.FloatField(null=True, blank=True)
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    ticket = models.CharField(max_length=100)
    fare = models.FloatField()
    cabin = models.CharField(max_length=50, null=True, blank=True)
    embarked = models.CharField(max_length=1)

    # String representation of the model
    def __str__(self):
        return f"{self.name} (ID: {self.passenger_id})"

    # Meta class for ordering the records by passenger_id
    class Meta:
        ordering = ['passenger_id']