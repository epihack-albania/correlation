import serpy
from django.utils.timezone import localtime


class HumanCaseSerializer(serpy.Serializer):
    case_count = serpy.IntField()
    residency_region = serpy.StrField()
    residency_district = serpy.StrField()
    residency_commune = serpy.StrField()
    residency_village = serpy.StrField()
    period = serpy.MethodField()
    disease = serpy.MethodField()
    confirm_count = serpy.IntField()
    probable_count = serpy.IntField()
    suspected_count = serpy.IntField()
    severity_level = serpy.StrField()

    def get_period(self, obj):
        return "{} - {}".format(localtime(obj.start_period).strftime('%d / %m / %Y'),
                                localtime(obj.end_period).strftime('%d / %m / %Y'))

    def get_disease(self, obj):
        return obj.disease.name


class AnimalCaseSerializer(serpy.Serializer):
    case_count = serpy.IntField()
    residency_region = serpy.StrField()
    residency_district = serpy.StrField()
    residency_commune = serpy.StrField()
    residency_village = serpy.StrField()
    period = serpy.MethodField()
    disease = serpy.MethodField()
    confirm_count = serpy.IntField()
    probable_count = serpy.IntField()
    suspected_count = serpy.IntField()
    severity_level = serpy.StrField()

    def get_period(self, obj):
        return "{} - {}".format(localtime(obj.start_period).strftime('%d / %m / %Y'),
                                localtime(obj.end_period).strftime('%d / %m / %Y'))

    def get_disease(self, obj):
        return obj.disease.name
