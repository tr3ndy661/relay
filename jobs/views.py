from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from celery.result import AsyncResult
from .tasks import send_welcome_email
from .models import Job 
import json

# Create your views here.
def send_email_to_user (request, user_email):

    new_job = Job.objects.create(
        celery_task_id= None,
        email= user_email,
    )
    task_result = send_welcome_email.delay(user_email, job_id=new_job.id)

    new_job.celery_task_id = task_result.id
    new_job.save()

    response_data = {
        'job_id' : new_job.id,
        'task_id' : task_result.id,
        'email' : user_email,
    }

    # return HttpResponse(f"Job queued! Task ID: {task_result.id}")
    return JsonResponse(response_data)

def check_task_status (request, task_id):
    result = AsyncResult(task_id)
    response_data = {
        'status': result.status,
        'result': str(result.result),
    }
    # return HttpResponse (f"Status: {result.status}, Result: {result.result}")
    return JsonResponse (response_data)

# listing all jobs view
def list_jobs (request):
    jobs = Job.objects.all()
    jobs_list = []
    for job in jobs:
        jobs_list.append({
            'id': job.id,
            'created_at': job.created_at,
            'started_at': job.started_at,
            'completed_at': job.completed_at,
            'email': job.email,
            'error_messages': job.error_messages,
        })

    return JsonResponse (jobs_list, safe=False)