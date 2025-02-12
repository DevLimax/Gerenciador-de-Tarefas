from django import forms
from .models import Status


class Add_task_form(forms.Form):
    title = forms.CharField(max_length=200,required=True)
    description = forms.CharField(max_length=200,required=False)