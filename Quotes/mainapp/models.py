from django.db import models

class QuoteModel(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=200)