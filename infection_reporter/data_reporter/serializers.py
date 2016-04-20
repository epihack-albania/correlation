import serpy


class HumanCaseSerializer(serpy.Serializer):
    case_count = serpy.IntField()
    disease = serpy.MethodField()
    hospitalization_avg = serpy.FloatField()
    sampling_avg = serpy.FloatField()
    laboratory_avg = serpy.FloatField()
    report_avg = serpy.FloatField()
    district = serpy.StrField()
    village = serpy.StrField()
    min_age = serpy.FloatField()
    max_age = serpy.FloatField()
    age_avg = serpy.FloatField()
    vaccination_rate = serpy.FloatField()
    death_rate = serpy.FloatField()
    recovery_rate = serpy.FloatField()
    sequela_rate = serpy.FloatField()
    attack_rate = serpy.FloatField()

    def get_disease(self, obj):
        return obj.disease.name


class AnimalCaseSerializer(serpy.Serializer):
    case_count = serpy.IntField()
    disease = serpy.MethodField()
    residency_district = serpy.StrField()
    residency_village = serpy.StrField()
    morbidity_rate = serpy.FloatField()
    mortality_rate = serpy.FloatField()
    fatality_rate = serpy.FloatField()

    def get_disease(self, obj):
        return obj.disease.name
