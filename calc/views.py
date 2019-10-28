from django.shortcuts import render
from .forms import Credit


def common_subjects(request):
    subject_list = (
        (10010010, "スタートアップセミナー", 1),
        (10110010, "総合英語Ｉａ", 2),
        (10110020, "総合英語Ｉｂ", 2),
    )
    subjects = []
    for element in subject_list:
        subjects.append(Credit(element[1], element[2]))
    return render(request, 'calc/common_subjects.html', {
        'subjects': subjects,
    })
