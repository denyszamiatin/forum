from django import forms
from django.core.exceptions import ValidationError

from .models import Message, Topic


class TopicForm(forms.Form):
    name = forms.CharField(label='Название', max_length=1000)

    def clean_name(self):
        name = self.cleaned_data['name']
        if '?' in name:
            raise ValidationError("Знак вопроса недопустим")
        return name


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5})
        }


class MessageEditForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('author', 'topic',)

MessageFormset = forms.inlineformset_factory(Topic,
                                             Message,
                                             fields=('text', ),
                                             extra=3)