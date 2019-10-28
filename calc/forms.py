from django import forms


class Credit(forms.Form):

    def __init__(self, subject_name, n_credits):
        self.subject_name = subject_name
        self.n_credits = n_credits
        self.doing = forms.BooleanField(
            required=False,
            disabled=False,
            label='doing',
        )

        self.done = forms.BooleanField(
            required=False,
            disabled=False,
            label='done',
        )
