from django import forms
from Records import models


class RecordsForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()




