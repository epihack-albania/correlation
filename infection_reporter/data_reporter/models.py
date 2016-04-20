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
        ordering = ['name']

    name = models.CharField('Name', max_length=255)
    incubation_period = models.PositiveIntegerField('Incubation period')
    symptoms = models.CharField('Symptoms', max_length=255)
    sequela = models.BooleanField('Sequela', default=False)
    human = models.BooleanField('Human', default=False)
    animal = models.BooleanField('Animal', default=False)
    urgent = models.BooleanField('Alarm', default=False)

    def __str__(self):
        return self.name


class HumanCase(StdModel):
    class Meta:
        db_table = 'human_case'
        verbose_name = 'Human Case'
        verbose_name_plural = 'Human Cases'

    case_count = models.PositiveIntegerField('Number of cases')
    hospitalization_avg = models.DecimalField('Hospitalization average time ', decimal_places=1, max_digits=3)
    sampling_avg = models.DecimalField('Sampling average time', decimal_places=1, max_digits=3)
    laboratory_avg = models.DecimalField('Laboratory average time', decimal_places=1, max_digits=3)
    report_avg = models.DecimalField('Report average time', decimal_places=1, max_digits=3)
    treatment_avg = models.DecimalField('Treatment average time', decimal_places=1, max_digits=3)
    district = models.CharField('District', max_length=255)
    village = models.CharField('Village', max_length=255)
    min_age = models.DecimalField('Min. Age', decimal_places=1, max_digits=4)
    max_age = models.DecimalField('Max Age', decimal_places=1, max_digits=4)
    age_avg = models.DecimalField('Average Age', decimal_places=1, max_digits=4)
    vaccination_rate = models.DecimalField('Vaccination Rate', decimal_places=1, max_digits=4)
    death_rate = models.DecimalField('Death Rate', decimal_places=1, max_digits=4)
    recovery_rate = models.DecimalField('Recovery Rate', decimal_places=1, max_digits=4)
    sequela_rate = models.DecimalField('Sequela Rate', decimal_places=1, max_digits=4)
    attack_rate = models.DecimalField('Attack Rate', decimal_places=1, max_digits=4)
    disease = models.ForeignKey(Disease, related_name='human_cases')

    def __str__(self):
        return "{} - {} - {}".format(self.disease, self.case_count, self.district)


class AnimalCase(StdModel):
    class Meta:
        db_table = 'animal_case'
        verbose_name = 'Animal Case'
        verbose_name_plural = 'Animal Cases'

    case_count = models.PositiveIntegerField('Number of cases')
    district = models.CharField('District', max_length=255)
    village = models.CharField('Village', max_length=255)
    morbidity_rate = models.DecimalField('Morbidity rate', max_digits=4, decimal_places=1)
    mortality_rate = models.DecimalField('Mortality rate', max_digits=4, decimal_places=1)
    fatality_rate = models.DecimalField('Fatality rate', max_digits=4, decimal_places=1)
    disease = models.ForeignKey(Disease, related_name='animal_cases')

    def __str__(self):
        return "{} - {} - {}".format(self.disease, self.case_count, self.district)
