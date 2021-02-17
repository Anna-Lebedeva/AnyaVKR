from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from . import models


class StudentAdmin(admin.ModelAdmin):
    fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'year', 'parent_name', 'course_id')
    form = UserCreationForm
    change_form = UserChangeForm

admin.site.register(models.Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'middle_name', 'picture', 'email', 'phone')
    form = UserCreationForm
    change_form = UserChangeForm


admin.site.register(models.Teacher, TeacherAdmin)


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Lesson, LessonAdmin)


class BoardAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Board, BoardAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Course, CourseAdmin)
