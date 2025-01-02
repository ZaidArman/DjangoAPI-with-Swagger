from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Passenger
from .serializers import PassengerSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

    @action(detail=False, methods=['get'])
    def survived(self, request):
        passengers = Passenger.objects.filter(survived=True)
        serializer = self.get_serializer(passengers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_class(self, request):
        pclass = request.query_params.get('pclass')
        if not pclass:
            return Response({'error': 'Please provide a class'}, status=status.HTTP_400_BAD_REQUEST)
        passengers = Passenger.objects.filter(pclass=pclass)
        serializer = self.get_serializer(passengers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add_passenger(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def expensive_tickets(self, request):
        passengers = Passenger.objects.filter(fare__gte=100)
        serializer = self.get_serializer(passengers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_gender(self, request):
        gender = request.query_params.get('gender')
        if not gender:
            return Response({'error': 'Please provide a gender'}, status=status.HTTP_400_BAD_REQUEST)
        passengers = Passenger.objects.filter(sex=gender)
        serializer = self.get_serializer(passengers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def family_travelers(self, request):
        passengers = Passenger.objects.filter(sibsp__gte=1)
        serializer = self.get_serializer(passengers, many=True)
        return Response(serializer.data)
