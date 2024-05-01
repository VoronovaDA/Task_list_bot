from django.db import models


class Tasks(models.Model):
    task_text = models.CharField(max_length=255)
