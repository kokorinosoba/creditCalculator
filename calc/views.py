from django.shortcuts import render
from django.views.generic import ListView
from .forms import Credit, SampleForm
from .models import Status


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


class Sample_Form(ListView):
    model = Status
    template_name = 'sample_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'status_list': Status.objects.order_by('subject_id'),
            'more_context': Status.objects.all(),
        })
        form_list = Status.objects.all()
        return context

    def get_queryset(self):
        return Status.objects.all()
