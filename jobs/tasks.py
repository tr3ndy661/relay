import time
from celery import shared_task
from .models import Job
from django.utils import timezone

@shared_task
def send_welcome_email (user_email, job_id):
        job = Job.objects.get(id = job_id)
        job.status = 'PROCESSING'
        job.started_at = timezone.now()
        job.save(update_fields=['status', 'started_at'])
                # job.save()
        try:
               print(f"Starting to send email to {user_email}...")
               time.sleep(5)
               print(f'Email sent to {user_email}')
               job.status = 'SUCCESS'
               job.completed_at = timezone.now()
               job.save(update_fields=['status', 'completed_at'])
               return f'Email sent to {user_email}'
        except Exception as e:
               job.status = 'FAILURE'
               job.completed_at = timezone.now()
               job.error_messages = str(e)
               job.save(update_fields=['status', 'completed_at', 'error_messages'])
               raise e



