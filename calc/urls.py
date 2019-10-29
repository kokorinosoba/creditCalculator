from django.urls import path
from . import views

urlpatterns = [
    path('common_subjects', views.common_subjects, name='common_subjects'),
    path('sample_form', views.sample_form, name='sample_form'),
]
