import csv
from django.core.management.base import BaseCommand
from titanic_app.models import Passenger

class Command(BaseCommand):
    help = 'Load Titanic data from titanic.csv'

    def handle(self, *args, **kwargs):
        with open('titanic.csv', 'r') as file:
            reader = csv.DictReader(file)
            Passenger.objects.all().delete()  # Clear existing data
            for row in reader:
                Passenger.objects.create(
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
        self.stdout.write(self.style.SUCCESS('Successfully loaded Titanic data'))
