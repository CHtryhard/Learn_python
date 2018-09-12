import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from AppTwo.models import UsersRecord
from faker import Faker

fakegen=Faker()

def populate(N=2):

    for entry in range(N):

        # create the fake date for that entry

        fake_email = fakegen.email()
        fake_name = fakegen.name()

        #create the new user entry
        user = UsersRecord.objects.get_or_create(name = fake_name, email=fake_email)[0]

if __name__ == '__main__':
    print("populate script!")
    populate(20)
    print("populate complete")
