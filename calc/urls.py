from django.urls import path
from . import views

urlpatterns = [
    path('common_subjects', views.common_subjects, name='common_subjects'),
]
