from django.urls import path

from . import views




from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('student/', views.student_form, name='student_form'),

    path('teacher/', views.teacher_form, name='teacher_form'),
]
