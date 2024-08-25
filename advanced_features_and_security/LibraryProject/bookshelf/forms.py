from django import forms
from .models import YourModel

class ExampleForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['field1', 'field2', 'field3']
