from django.urls import path

from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/calendar/', CalendarView.as_view(), name='calendar'),
    path('profile/lesson/', LessonView.as_view(), name='lesson'),
    path('profile/lesson/add', AddLessonView.as_view(), name='add_lesson'),
    path('profile/lesson/edit', EditLessonView.as_view(), name='edit_lesson'),
    path('profile/finance/', FinanceView.as_view(), name='finance'),
]
