from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render

from data_reporter.models import HumanCase, AnimalCase, Disease
from data_reporter.serializers import HumanCaseSerializer, AnimalCaseSerializer


def index(request):
    return render(request, 'data_reporter/index.html')


def get_disease_view(request, disease_pk):
    disease = Disease.objects.get(pk=disease_pk)
    return render(request, 'data_reporter/index.html', context={'active': disease.name})


def get_human_cases(request, disease_pk):
    human_cases = HumanCase.objects.filter(disease_id=disease_pk)
    return JsonResponse({'data': HumanCaseSerializer(human_cases, many=True).data})


def get_animal_cases(request, disease_pk):
    human_cases = AnimalCase.objects.filter(disease_id=disease_pk)
    return JsonResponse({'data': AnimalCaseSerializer(human_cases, many=True).data})
