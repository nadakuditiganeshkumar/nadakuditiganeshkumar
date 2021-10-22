import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE','pages.settings')

import django
django.setup()

##Fake Pop Script

from layout.models import *
from faker import Faker

fakegen=Faker()
topics=['UI','PYTHON','JAVA','DOT NET','C++','C','Embedded']
def add_topic():
    t=Department.objects.get_or_create(department_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        top = add_topic()
        # create the Fake data for the entry
        fake_employee_name = fakegen.name()
        fake_dob = fakegen.date()
        fake_joining_date = fakegen.date()
        fake_salary =round(random.uniform(10000,25600),2)
        fake_weight = round(random.uniform(10,99),2)
        fake_manager = fakegen.name()
        fake_city = fakegen.name()
        # create the new webpage entry
        webpg = Employee.objects.get_or_create(employee_name=fake_employee_name,dob=fake_dob,joining_date=fake_joining_date,manager=fake_manager,weight=fake_weight,salary=fake_salary,department=top,city=fake_city)[0]

if __name__=='__main__':
    print("Populating Database")
    populate(20)
    print("Populate complate")