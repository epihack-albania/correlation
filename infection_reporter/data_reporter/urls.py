from django.conf.urls import url

from data_reporter.views import get_human_cases, get_animal_cases, index

urlpatterns = [
    url(r'index/', index, name='index'),
    url(r'human/cases/', get_human_cases, name='human-cases'),
    url(r'animal/cases/', get_animal_cases, name='animal-cases'),
]
