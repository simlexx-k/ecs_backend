from django.core.management.base import BaseCommand
from faker import Faker
from ecs.models import Employee
import phonenumbers

class Command(BaseCommand):
    help = 'Populate employees in the database'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # Generate 10 fake employee records
            name = fake.name()
            age = fake.random_int(min=18, max=65)
            phone = fake.phone_number()

            # Parse and format the phone number using phonenumbers
            parsed_phone = phonenumbers.parse(phone, "KE")  # Assuming numbers are US numbers
            formatted_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)

            email = fake.email()
            Employee.objects.create(name=name, age=age, phone=formatted_phone, email=email)
