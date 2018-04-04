import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_django.settings')
import django
django.setup()


## FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topcis = ['Search', 'Social', 'Marketplace', 'News', 'Games','Education']

def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topcis))[0]
	t.save()
	return t

def populate(N=6):
	for entry in range(N):

		# get the topic for entry
		top = add_topic()

		# create fake data for that entry
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		# Create a new web page entry
		webpg = Webpage.objects.get_or_create(topic=top, url = fake_url,
		                                      name =fake_name)[0]

		# create a fake access record forthat webpage
		acc_rec =AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
	print('populating script!')
	populate(20)
	print('populating complete!')