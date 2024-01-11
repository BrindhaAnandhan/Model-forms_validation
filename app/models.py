from django.db import models
from django.core import validators
from django import forms
#from forms import validators

# Create your models here.
def check(value):
    if value.lower()[0] == 'a':
        raise forms.ValidationError("invalid")
    


class Student(models.Model):
    Sname = models.CharField(max_length =100, primary_key = True, validators=[check])
    Sage = models.IntegerField()
    Smobile = models.CharField(max_length = 10, validators = [validators.RegexValidator('[6-9]\d{9}')] )

    def __str__(self) -> str:
        return self.Sname
    