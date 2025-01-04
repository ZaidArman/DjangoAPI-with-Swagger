from rest_framework import serializers
from .models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

    # age validation
    def validate_age(self, value):
        if value and value < 0:
            raise serializers.ValidationError("Age cannot be negative")
        return value

    # fare validation
    def validate_fare(self, value):
        if value < 0:
            raise serializers.ValidationError("Fare cannot be negative")
        return value