from django.test import TestCase
from rest_framework.test import APIClient
from .models import Passenger

class PassengerAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Passenger.objects.create(passenger_id=1, survived=True, pclass=1, name="Test Passenger", sex="male", age=30, sibsp=0, parch=0, ticket="12345", fare=100.0, cabin="B1", embarked="S")

    def test_list_passengers(self):
        response = self.client.get('/api/passengers/')
        self.assertEqual(response.status_code, 200)

    def test_add_passenger(self):
        payload = {
            "passenger_id": 2,
            "survived": False,
            "pclass": 2,
            "name": "New Passenger",
            "sex": "female",
            "age": 25,
            "sibsp": 1,
            "parch": 0,
            "ticket": "67890",
            "fare": 50.0,
            "cabin": "C1",
            "embarked": "Q"
        }
        response = self.client.post('/api/passengers/add_passenger/', payload, format='json')
        self.assertEqual(response.status_code, 201)
