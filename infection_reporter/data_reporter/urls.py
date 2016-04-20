from django.conf.urls import url

from data_reporter.views import get_human_cases, get_animal_cases, index, get_disease_view

urlpatterns = [
    url(r'index/', index, name='index'),
    url(r'disease/(?P<disease_pk>\d+)/$', get_disease_view, name='disease'),
    url(r'human/cases/(?P<disease_pk>\d+)/$', get_human_cases, name='human-cases'),
    url(r'animal/cases/(?P<disease_pk>\d+)/$', get_animal_cases, name='animal-cases'),
]
