from django.urls import path

from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/calendar/', ProfileView.as_view(template_name='profile/calendar.html'), name='calendar'),
    path('profile/lesson/', ProfileView.as_view(template_name='profile/lesson.html'), name='lesson'),
    path('profile/finance/', ProfileView.as_view(template_name='profile/finance.html'), name='finance'),
]
