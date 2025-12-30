# URL patterns for user authentication
# 用户认证的 URL 模式

from django.urls import path, include
from . import views

# App namespace / 应用命名空间
app_name = 'accounts'

urlpatterns = [
    # Include Django's default authentication URLs (login, logout, etc.)
    # 包含 Django 默认的认证 URL（登录、登出等）
    path('', include('django.contrib.auth.urls')),

    # Custom user registration URL / 自定义用户注册 URL
    path('register/', views.register, name='register'),
]