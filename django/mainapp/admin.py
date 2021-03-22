from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from . import models
from .models import PreStudent


class StudentAdmin(admin.ModelAdmin):
    fields = ('prestudent_id', 'username', 'password1', 'password2', 'first_name', 'last_name',
              'email', 'phone', 'grade', 'parent_name', 'student_teacher')
    form = UserCreationForm
    change_form = UserChangeForm

    def prestudent_id(self, obj):
        return obj.prestudent_id

    def first_name(self, obj):
        return PreStudent.objects.get(id=obj.prestudent_id).first_name


admin.site.register(models.Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    fields = ('username', 'password1', 'password2', 'first_name', 'last_name',
              'middle_name', 'picture', 'email', 'phone')
    form = UserCreationForm
    change_form = UserChangeForm
    list_display = ('username', 'get_full_name')


admin.site.register(models.Teacher, TeacherAdmin)


class PreStudentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'phone', 'email')


admin.site.register(models.PreStudent, PreStudentAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('student', 'board', 'subject', 'time_start', 'duration', 'teacher', 'board')


admin.site.register(models.Lesson, LessonAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Course, CourseAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'grade', 'category')
    search_fields = ('title', 'author')
    list_filter = ('grade', 'category')


admin.site.register(models.Book, BookAdmin)
