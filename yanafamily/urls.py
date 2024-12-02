from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bot_user.urls')),  # Предполагается, что bot_user имеет urls.py
]
