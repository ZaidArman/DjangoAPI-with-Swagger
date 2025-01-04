# API views for the Titanic app

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Passenger
from .serializers import PassengerSerializer

class PassengerListCreateView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class SurvivedPassengersView(generics.ListAPIView):
    serializer_class = PassengerSerializer

    # queryset for only survived passengers
    def get_queryset(self):
        return Passenger.objects.filter(survived=True)

class PassengersByClassView(generics.ListAPIView):
    serializer_class = PassengerSerializer

    # queryset for passengers by class
    def get_queryset(self):
        pclass = self.kwargs['pclass']
        return Passenger.objects.filter(pclass=pclass)

class PassengersByGenderView(generics.ListAPIView):
    serializer_class = PassengerSerializer

    # queryset for passengers by gender
    def get_queryset(self):
        gender = self.kwargs['gender']
        return Passenger.objects.filter(sex=gender)

class ExpensiveTicketsView(generics.ListAPIView):
    serializer_class = PassengerSerializer

    # queryset for expensive tickets
    def get_queryset(self):
        return Passenger.objects.filter(fare__gte=100)

class FamilyTravelersView(generics.ListAPIView):
    serializer_class = PassengerSerializer

    # queryset for family travelers
    def get_queryset(self):
        return Passenger.objects.filter(sibsp__gte=1)