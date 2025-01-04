from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Passenger

class PassengerAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create test passenger
        self.test_passenger = Passenger.objects.create(
            passenger_id=1,
            survived=True,
            pclass=1,
            name="Test Passenger",
            sex="male",
            age=30,
            sibsp=0,
            parch=0,
            ticket="12345",
            fare=100.0,
            cabin="B1",
            embarked="S"
        )
        
        # Valid passenger data for testing
        self.valid_passenger = {
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
        
        # Invalid passenger data for testing
        self.invalid_passenger = {
            "passenger_id": 3,
            "survived": "invalid",  # Should be boolean
            "pclass": "invalid",    # Should be integer
            "name": "",            # Empty name
            "sex": "invalid",      # Invalid gender
            "age": -5,            # Negative age
            "sibsp": -1,          # Negative siblings
            "parch": "invalid",    # Should be integer
            "ticket": "",         # Empty ticket
            "fare": -50.0,        # Negative fare
            "embarked": ""        # Empty embarked
        }

    # Test cases for Passenger list create 
    def test_list_passengers(self):
        """Test retrieving list of passengers"""
        url = reverse('passenger-list-create')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Passenger")

    # Test cases for Passenger list create valid data
    def test_create_valid_passenger(self):
        """Test creating a new passenger with valid data"""
        url = reverse('passenger-list-create')
        response = self.client.post(url, self.valid_passenger, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passenger.objects.count(), 2)
        self.assertEqual(Passenger.objects.get(passenger_id=2).name, "New Passenger")

    # Test cases for Passenger list create invalid data
    def test_create_invalid_passenger(self):
        """Test creating a new passenger with invalid data"""
        url = reverse('passenger-list-create')
        response = self.client.post(url, self.invalid_passenger, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Passenger.objects.count(), 1)

    # Test cases for a single Passenger detail
    def test_get_single_passenger(self):
        """Test retrieving a single passenger"""
        url = reverse('passenger-detail', kwargs={'pk': self.test_passenger.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Passenger")

    # Test cases for Passenger detail update
    def test_update_passenger(self):
        """Test updating an existing passenger"""
        url = reverse('passenger-detail', kwargs={'pk': self.test_passenger.id})
        updated_data = {
            "passenger_id": 1,
            "name": "Updated Name",
            "survived": True,
            "pclass": 1,
            "sex": "male",
            "age": 35,
            "sibsp": 0,
            "parch": 0,
            "ticket": "12345",
            "fare": 100.0,
            "cabin": "B1",
            "embarked": "S"
        }
        response = self.client.put(url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Passenger.objects.get(id=self.test_passenger.id).name, "Updated Name")

    # Test cases for Passenger detail delete
    def test_delete_passenger(self):
        """Test deleting a passenger"""
        url = reverse('passenger-detail', kwargs={'pk': self.test_passenger.id})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Passenger.objects.count(), 0)

    # Test cases for survived passengers API views
    def test_get_survived_passengers(self):
        """Test retrieving survived passengers"""
        url = reverse('survived-passengers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(response.data[0]['survived'])

    # Test cases for passengers by class API views
    def test_get_passengers_by_class(self):
        """Test retrieving passengers by class"""
        url = reverse('passengers-by-class', kwargs={'pclass': 1})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['pclass'], 1)

    # Test cases for passengers by gender API views
    def test_get_passengers_by_gender(self):
        """Test retrieving passengers by gender"""
        url = reverse('passengers-by-gender', kwargs={'gender': 'male'})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['sex'], 'male')

    # Test cases for expensive tickets API views
    def test_get_expensive_tickets(self):
        """Test retrieving passengers with expensive tickets"""
        url = reverse('expensive-tickets')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(response.data[0]['fare'] >= 100.0)

    # Test cases for family travelers API views
    def test_get_family_travelers(self):
        """Test retrieving family travelers"""
        url = reverse('family-travelers')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # Our test passenger has sibsp=0

    # Test cases for non-existent passenger detail
    def test_nonexistent_passenger(self):
        """Test retrieving a non-existent passenger"""
        url = reverse('passenger-detail', kwargs={'pk': 999})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Test cases for Passenger model
class PassengerModelTest(TestCase):
    """Test cases for Passenger model"""
    
    def test_passenger_creation(self):
        """Test creating a passenger"""
        passenger = Passenger.objects.create(
            passenger_id=1,
            survived=True,
            pclass=1,
            name="Test Passenger",
            sex="male",
            age=30,
            sibsp=0,
            parch=0,
            ticket="12345",
            fare=100.0,
            cabin="B1",
            embarked="S"
        )
        self.assertTrue(isinstance(passenger, Passenger))
        self.assertEqual(passenger.__str__(), "Test Passenger (ID: 1)")

    # Test cases for Passenger model update
    def test_passenger_update(self):
        """Test updating a passenger"""
        passenger = Passenger.objects.create(
            passenger_id=1,
            survived=True,
            pclass=1,
            name="Test Passenger",
            sex="male",
            age=30,
            sibsp=0,
            parch=0,
            ticket="12345",
            fare=100.0,
            cabin="B1",
            embarked="S"
        )
        passenger.name = "Updated Name"
        passenger.save()
        updated_passenger = Passenger.objects.get(id=passenger.id)
        self.assertEqual(updated_passenger.name, "Updated Name")