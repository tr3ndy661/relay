from django.db import models


# Create your models here.
class Job (models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'pending'),
        ('PROCESSING', 'processing'),
        ('SUCCESS', 'success'),
        ('FAILURE', 'failure'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    # adding time stamps
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null = True, blank = True)
    completed_at = models.DateTimeField(null = True, blank = True)

    # defining the uuid, email and error message fileds
    celery_task_id = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()

    error_messages = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.email} - {self.status}"

