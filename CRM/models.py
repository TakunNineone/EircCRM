from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tasks_status(models.Model):
    task_status_id = models.AutoField(primary_key=True)
    task_status = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.task_status


class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.task_name


class Cases(models.Model):
    case_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    task_status = models.ForeignKey(Tasks_status, to_field='task_status_id', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return Tasks.task_name
