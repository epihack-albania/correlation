from django.db import models


# Create your models here.
class StdModel(models.Model):
    class Meta:
        app_label = 'data_reporter'
        abstract = True


class Disease(StdModel):
    class Meta:
        db_table = 'disease'
        verbose_name = 'Disease'
        verbose_name_plural = 'Disease'

    name = models.CharField('Name', max_length=255)
    incubation_period = models.PositiveIntegerField('Incubation period')
    symptoms = models.CharField('Symptoms', max_length=255)

    def __str__(self):
        return self.name


class HumanCase(StdModel):
    class Meta:
        db_table = 'human_case'
        verbose_name = 'Human Case'
        verbose_name_plural = 'Human Cases'

    case_count = models.PositiveIntegerField('Number of cases')
    residency_region = models.CharField('Region', max_length=255)
    residency_district = models.CharField('District', max_length=255)
    residency_commune = models.CharField('Commune', max_length=255)
    residency_village = models.CharField('Village', max_length=255)
    start_period = models.DateTimeField('Start Date')
    end_period = models.DateTimeField('End Date')
    disease = models.ForeignKey(Disease)
    confirm_count = models.PositiveIntegerField('Confirmed')
    probable_count = models.PositiveIntegerField('Probable')
    suspected_count = models.PositiveIntegerField('Suspected')
    severity_level = models.CharField('Severity Level', max_length=255)

    def __str__(self):
        return "{} - {} - {}".format(self.disease, self.case_count, self.residency_region)


class AnimalCase(StdModel):
    class Meta:
        db_table = 'animal_case'
        verbose_name = 'Animal Case'
        verbose_name_plural = 'Animal Cases'

    case_count = models.PositiveIntegerField('Number of cases')
    residency_region = models.CharField('Region', max_length=255)
    residency_district = models.CharField('District', max_length=255)
    residency_commune = models.CharField('Commune', max_length=255)
    residency_village = models.CharField('Village', max_length=255)
    start_period = models.DateTimeField('Start Date')
    end_period = models.DateTimeField('End Date')
    disease = models.ForeignKey(Disease)
    confirm_count = models.PositiveIntegerField('Confirmed')
    probable_count = models.PositiveIntegerField('Probable')
    suspected_count = models.PositiveIntegerField('Suspected')
    severity_level = models.CharField('Severity Level', max_length=255)
