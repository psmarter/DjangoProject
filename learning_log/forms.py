from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """A form for creating and updating topics."""

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}  # No label for the text field

class EntryForm(forms.ModelForm):
    """A form for creating and updating entries."""

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}  # No label for the text field
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # Wider text area