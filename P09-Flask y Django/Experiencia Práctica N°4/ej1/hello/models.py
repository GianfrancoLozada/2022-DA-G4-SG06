from django.db import models

class Members(models.Model):

    num1 = models.IntegerField(max_length=2);
    num2 = models.IntegerField(max_length=2);
    suma = models.IntegerField(max_length=3);
    resta = models.IntegerField(max_length=3);
    multi = models.IntegerField(max_length=5);
    div = models.FloatField(max_length=5);
    poten = models.IntegerField(max_length=255);