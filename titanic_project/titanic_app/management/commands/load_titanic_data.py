import csv
from django.core.management.base import BaseCommand
from titanic_app.models import Passenger

class Command(BaseCommand):
    help = 'Load Titanic data from titanic.csv'

    def handle(self, *args, **kwargs):
        try:
            # Load data from titanic.csv
            with open('titanic.csv', 'r') as file:
                reader = csv.DictReader(file)
                Passenger.objects.all().delete()  # Clear existing data
                
                # Create Passenger objects from CSV data
                passengers = [
                    Passenger(
                        passenger_id=int(row['PassengerId']),
                        survived=row['Survived'] == '1',
                        pclass=int(row['Pclass']),
                        name=row['Name'],
                        sex=row['Sex'],
                        age=float(row['Age']) if row['Age'] else None,
                        sibsp=int(row['SibSp']),
                        parch=int(row['Parch']),
                        ticket=row['Ticket'],
                        fare=float(row['Fare']),
                        cabin=row['Cabin'] if row['Cabin'] else None,
                        embarked=row['Embarked'],
                    )
                    for row in reader
                ]
                
                # Bulk insert Passenger objects
                Passenger.objects.bulk_create(passengers)
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(passengers)} passengers'))
                
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Error: titanic.csv file not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))