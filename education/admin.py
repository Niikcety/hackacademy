from django.contrib import admin

from education.models import Course, Lecture, Task


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_duration', 'start_date', 'end_date')

    def get_duration(self, obj):
        if obj.duration:
            return '{} weeks'.format(obj.duration.days // 7)

        return 'N/A'

    get_duration.short_description = 'Duration'


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('lecture_id', 'name', 'week', 'course', 'url')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date', 'course', 'lecture')
