from django import forms
from django.core.exceptions import ValidationError


class TopicForm(forms.Form):
    name = forms.CharField(label='Название', max_length=1000)

    def clean_name(self):
        name = self.cleaned_data['name']
        if '?' in name:
            raise ValidationError("Знак вопроса недопустим")
        return name
