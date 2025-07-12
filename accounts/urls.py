from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # Include the default auth URLs
    path('', include('django.contrib.auth.urls')),

    # Custom user registration URL
    path('register/', views.register, name='register'),
    #
    # # Custom profile URL
    # path('profile/', include('accounts.views.profile'), name='profile'),
]