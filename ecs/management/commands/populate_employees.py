# management/commands/populate_employees.py

from django.core.management.base import BaseCommand
from faker import Faker
from ecs.models import Employee

class Command(BaseCommand):
    help = 'Populate employees in the database'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # Generate 10 fake employee records
            name = fake.name()
            age = fake.random_int(min=18, max=65)
            phone = fake.phone_number()
            email = fake.email()
            # Manually append the country code for Kenya (+254)
            phone_ke = "+254" + phone[1:]  # Remove the leading zero from the generated phone number
            
            # Add other fields as needed
            Employee.objects.create(name=name, age=age, phone = phone_ke, email=email)
