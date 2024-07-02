from django.contrib import admin
from django.urls import path, include
from .views import health_check, thank_you

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brief/', include('website_brief.urls')),
    path('health/', health_check, name='health_check'),
    path('thank_you/', thank_you, name='thank_you'),
]
