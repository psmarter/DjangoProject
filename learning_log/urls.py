# URL patterns for Learning Log application
# 学习日志应用的 URL 模式

from django.urls import path
from . import views

# App namespace / 应用命名空间
app_name = 'learning_log'

urlpatterns = [
    # Home page / 主页
    path('', views.index, name='index'),
    
    # Page to show all topics / 显示所有主题的页面
    path('topics/', views.topics, name='topics'),
    
    # Detail page for a single topic / 单个主题的详情页
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Page for adding a new topic / 添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    
    # Page for adding a new entry / 添加新条目的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    # Page for editing an entry / 编辑条目的页面
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]