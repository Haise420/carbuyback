from django.db import models

CAR_BRAND = []
CAR_MODEL = []
BODY_TYPE = []

# Create your models here.
class Pitanje(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    car_brand = models.CharField(max_length=30, choices=CAR_BRAND)
    car_model = models.CharField(max_length=30, choices=CAR_MODEL)
    body_type = models.CharField(max_length=30, choices=BODY_TYPE)
    question = models.TextField(max_length=2500)