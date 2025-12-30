# Forms for Learning Log application
# 学习日志应用的表单

from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """
    A form for creating and updating topics.
    用于创建和更新主题的表单。
    """

    class Meta:
        model = Topic
        # Only include the text field / 只包含文本字段
        fields = ['text']
        # No label for cleaner UI / 不显示标签以获得更简洁的界面
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """
    A form for creating and updating entries.
    用于创建和更新条目的表单。
    """

    class Meta:
        model = Entry
        # Only include the text field / 只包含文本字段
        fields = ['text']
        # No label for cleaner UI / 不显示标签以获得更简洁的界面
        labels = {'text': ''}
        # Wider text area for better editing experience / 更宽的文本区域以获得更好的编辑体验
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}