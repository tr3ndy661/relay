from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from .tasks import send_welcome_email
from .models import Job 

# Create your views here.
def send_email_to_user (request, user_email):

    new_job = Job.objects.create(
        celery_task_id= None,
        email= user_email,
    )
    task_result = send_welcome_email.delay(user_email, job_id=new_job.id)

    new_job.celery_task_id = task_result.id
    new_job.save()

    return HttpResponse(f"Job queued! Task ID: {task_result.id}")

def check_task_status (request, task_id):
    result = AsyncResult(task_id)
    return HttpResponse (f"Status: {result.status}, Result: {result.result}")