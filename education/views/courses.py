from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from education.models import Course, Lecture, Task


def list(request):
    return render(request, 'courses/list.html', {'courses': Course.objects.all()})


def detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    c_name = course.name
    return render(request, 'courses/detail.html', {'course': course,
                                                   'lectures': Lecture.objects.filter(course__name=c_name),
                                                   'tasks': Task.objects.filter(course__name=c_name)})


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'courses/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:courses:detail', kwargs={'course_id': self.object.id})
