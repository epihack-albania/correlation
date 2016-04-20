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
    sequela = models.BooleanField('Sequela', default=False)
    human = models.BooleanField('Human', default=False)
    animal = models.BooleanField('Animal', default=False)

    def __str__(self):
        return self.name


class HumanCase(StdModel):
    class Meta:
        db_table = 'human_case'
        verbose_name = 'Human Case'
        verbose_name_plural = 'Human Cases'

    case_count = models.PositiveIntegerField('Number of cases')
    hospitalization_avg = models.PositiveIntegerField('Hospitalization average time ')
    sampling_avg = models.PositiveIntegerField('Sampling average time')
    laboratory_avg = models.PositiveIntegerField('Laboratory average time')
    report_avg = models.PositiveIntegerField('Report average time')
    district = models.CharField('District', max_length=255)
    village = models.CharField('Village', max_length=255)
    min_age = models.DecimalField('Min. Age', decimal_places=1, max_digits=3)
    max_age = models.DecimalField('Max Age', decimal_places=1, max_digits=3)
    avg_age = models.DecimalField('Average Age', decimal_places=1, max_digits=3)
    vaccination_rate = models.DecimalField('Vaccination Rate', decimal_places=1, max_digits=3)
    death_rate = models.DecimalField('Death Rate', decimal_places=1, max_digits=3)
    recovery_rate = models.DecimalField('Recovery Rate', decimal_places=1, max_digits=3)
    sequela_rate = models.DecimalField('Sequela Rate', decimal_places=1, max_digits=3)
    attack_rate = models.DecimalField('Attack Rate', decimal_places=1, max_digits=3)
    disease = models.ForeignKey(Disease)

    def __str__(self):
        return "{} - {} - {}".format(self.disease, self.case_count, self.district)


class AnimalCase(StdModel):
    class Meta:
        db_table = 'animal_case'
        verbose_name = 'Animal Case'
        verbose_name_plural = 'Animal Cases'

    case_count = models.PositiveIntegerField('Number of cases')
    district = models.CharField('District', max_length=255)
    village = models.CharField('District', max_length=255)
    morbidity_rate = models.DecimalField('Morbidity rate', max_digits=3, decimal_places=2)
    mortality_rate = models.DecimalField('Mortality rate', max_digits=3, decimal_places=2)
    fatality_rate = models.DecimalField('Fatality rate', max_digits=3, decimal_places=2)
    disease = models.ForeignKey(Disease)

    def __str__(self):
        return "{} - {} - {}".format(self.disease, self.case_count, self.district)
