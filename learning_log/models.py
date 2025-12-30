# Django models for Learning Log application
# 学习日志应用的 Django 模型

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """
    A topic the user is learning about.
    用户正在学习的主题。
    """
    # Topic name, max 200 characters / 主题名称，最多200个字符
    text = models.CharField(max_length=200)
    
    # Timestamp when topic was created / 主题创建时间戳
    date_added = models.DateTimeField(auto_now_add=True)
    
    # User who owns this topic / 拥有此主题的用户
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the model.
        返回模型的字符串表示。
        """
        return self.text


class Entry(models.Model):
    """
    Something specific learned about a topic.
    关于某个主题的具体学习内容。
    """
    # The topic this entry belongs to / 此条目所属的主题
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    # The actual learning content / 实际的学习内容
    text = models.TextField()
    
    # Timestamp when entry was created / 条目创建时间戳
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Plural name for admin interface / 管理界面的复数名称
        verbose_name_plural = 'entries'

    def __str__(self):
        """
        Return a string representation of the model.
        返回模型的字符串表示。
        
        Returns first 50 characters of text with ellipsis if longer.
        如果文本超过50个字符，返回前50个字符并加省略号。
        """
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text