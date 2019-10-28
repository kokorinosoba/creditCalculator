from django.shortcuts import render
from .forms import Credit


def common_subjects(request):
    subject = Credit()
    return render(request, 'calc/common_subjects.html', {
        'subject': subject,
    })
