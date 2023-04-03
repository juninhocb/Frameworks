from django.urls import path
from .views import *

#its important naming the routes, in cases we want to use these endpoints
#in other modules of our project
urlpatterns = [
    path('hello/', hello_world, name='hello'),
    path('create_person/', create_person, name='create_p'),
    path('create_office/', create_office, name='create_o'),
    path('offices/', read_all_offices, name='read_all_o'),
    path('offices/<int:office_id>', read_an_office, name='read_an_o'),
    path('people/', read_all_persons, name='read_all_p'),
    path('person/<int:person_id>', read_a_person, name='read_a_p'),
    path('update_office/<int:office_id>', update_an_office, name='update_an_o'),
    path('update_person/<int:person_id>', update_a_person, name='update_a_p'),
    path('delete_office/<int:office_id>', delete_an_office, name='delete_an_o'),
    path('delete_person/<int:person_id>', delete_a_person, name='delete_a_p'),
]