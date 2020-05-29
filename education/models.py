from django.db import models
from django.utils import timezone
import requests


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return 'Course "{}"'.format(self.name)

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date


class Lecture(models.Model):
    lecture_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    week = models.IntegerField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    url = models.TextField()

    def __str__(self):
        return 'Lecture "{}"'.format(self.name)


class Task(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    lecture = models.ForeignKey('Lecture', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Task "{}"'.format(self.name)


class Solution(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    date = models.DateTimeField()
    url = models.TextField()

    def __str__(self):
        return 'Solution for "{}"'.format(self.task.name)

    def validate_url(self):
        r = requests.get(self.url)
        if r.headers['server'] == 'GitHub.com':
            return True
        return False

    def clean(self, *args, **kwargs):
        if self.validate_url():
            super(Solution, self).clean(*args, **kwargs)
        else:
            raise ValueError('This is not github repo')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Solution, self).save(*args, **kwargs)
