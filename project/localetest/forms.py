from django import forms

from project.localetest.models import BasicModel


class BasicForm(forms.ModelForm):
    class Meta:
        model = BasicModel
        fields = '__all__'
