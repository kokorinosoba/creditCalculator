from django import forms


class Credit(forms.Form):
    subject_name = None
    doing = forms.BooleanField(
        required=False,
        disabled=False,
        label='doing',
    )
    done = forms.BooleanField(
        required=False,
        disabled=False,
        label='done',
    )
