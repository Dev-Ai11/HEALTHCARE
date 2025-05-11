from django.db import models


class patient(models.Model):
    Name=models.CharField(max_length=200)

