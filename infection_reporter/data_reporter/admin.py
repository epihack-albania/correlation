from django.contrib import admin

from data_reporter.models import Disease, HumanCase, AnimalCase

admin.site.register(Disease)
admin.site.register(HumanCase)
admin.site.register(AnimalCase)
