import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_django.settings')
import django
django.setup()

from first_app.models import User
from faker import Faker

fakegen =Faker()
def populate(N=10):
	for i in range(N):
		fake_first_name = fakegen.name()
		fake_second_name = fakegen.name()
		fake_email = fakegen.address()
		User.objects.get_or_create(first_name=fake_first_name,
		                           last_name = fake_second_name,
		                           email =fake_email)


if __name__ == '__main__':
	print('populating')
	populate(30)
	print("ending.")