from django.http import JsonResponse
from django.shortcuts import render

from data_reporter.models import HumanCase, AnimalCase
from data_reporter.serializers import HumanCaseSerializer, AnimalCaseSerializer


def index(request):
    return render(request, 'data_reporter/index.html')


def get_human_cases(request):
    human_cases = HumanCase.objects.all()
    return JsonResponse({'data': HumanCaseSerializer(human_cases, many=True).data})


def get_animal_cases(request):
    human_cases = AnimalCase.objects.all()
    return JsonResponse({'data': AnimalCaseSerializer(human_cases, many=True).data})
