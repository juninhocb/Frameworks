from django.db import models
from .enums import Nationality

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

class Office(BaseModel):
    name = models.CharField(max_length=30, null=False, default="unknown", unique=True)

class Person(BaseModel):
    name = models.CharField(max_length=50, null=False, default="unknown", unique=True)
    age = models.IntegerField(null=False, default=0)
    isRetired =  models.BooleanField(null=False, default=False)
    nationality = models.CharField(max_length=2, choices= Nationality.choices, null=False, default= Nationality.PORTUGUESE)
    idOffice = models.ForeignKey(Office, on_delete=models.CASCADE)

