from django.db import models

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

class patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, default='name')
    mobile = models.CharField(null=True)
    address = models.TextField(null=True)
    detail = models.TextField(null=True)
    medicine_detail = models.TextField(null=True)
    note = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    next_visit = models.IntegerField(default=0)

    def __str__(self):
        return self.name
