from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(
        null=False, validators=[MinValueValidator(0), MaxValueValidator(150)])
    sex = models.BooleanField(null=False)
    cest_pain_type = models.IntegerField(
        null=False, validators=[MinValueValidator(0), MaxValueValidator(3)])
    resting_blood_pressure = models.IntegerField(
        null=False, validators=[MinValueValidator(0)])
    cholestrol = models.IntegerField(
        null=False, validators=[MinValueValidator(0)])
    fasting_blood_sugar = models.BooleanField(default=False)
    rest_ecg = models.IntegerField(
        null=False, validators=[MinValueValidator(0), MaxValueValidator(2)])
    max_heart_rate = models.IntegerField(
        null=False, validators=[MinValueValidator(0)])
    exercise_induced_angina = models.BooleanField(null=False)
    oldpeak = models.DecimalField(null=False, max_digits=3, decimal_places=1)
    slope = models.IntegerField(
        null=False, validators=[MinValueValidator(0), MaxValueValidator(2)])
    vessels_colored_by_fluroscopy = models.IntegerField(
        null=False, validators=[MinValueValidator(0), MaxValueValidator(4)])
    thallium_stress_test = models.IntegerField(
        null=False, validators=[MinValueValidator(0), MaxValueValidator(3)])
    prediction_result = models.BooleanField(default=False)

    def Patient():
        return

    def __str__(self):
        return super().__str__()  


    