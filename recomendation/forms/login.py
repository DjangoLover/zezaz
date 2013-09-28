# -*- coding: utf-8
from django import forms
from recomendation.models import User


def clean(self):
    super(LogInForm, self).clean()

    if not self.cleaned_data.get('username') and \
       not self.cleaned_data.get('password'):
        raise ValidationError(_(u'All fields are required'))

    return self.cleaned_data


class LogInForm(forms.ModelForm):
    class Meta:
        model = User