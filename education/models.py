from django.db import models
from django.utils import timezone


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
