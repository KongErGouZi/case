from django.contrib import admin
from .models import Course, CourseSection, CourseCategory, CourseChapter, Teacher

admin.site.register(Course)
admin.site.register(CourseSection)
admin.site.register(CourseCategory)
admin.site.register(CourseChapter)
admin.site.register(Teacher)
