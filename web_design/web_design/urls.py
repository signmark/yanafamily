from django.contrib import admin
from django.urls import include, path
from website_brief import views as brief_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brief/', include('website_brief.urls')),
    # path('thank_you/', brief_views.thank_you, name='thank_you'),
]
