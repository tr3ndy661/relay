from django.db import models

# Create your models here.
class Job (models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'pending'),
        ('SUCCESS', 'success'),
        ('FAILURE', 'failure'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    # adding time stamps