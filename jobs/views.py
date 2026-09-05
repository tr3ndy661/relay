from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from .tasks import send_welcome_email

# Create your views here.
def send_email_to_user (request, user_email):
    send_email = send_welcome_email.delay(user_email)
    return HttpResponse(send_email)

def check_task_status (request, task_id):
    result = AsyncResult(task_id)
    return HttpResponse (f"Status: {result.status}, Result: {result.result}")