from django.urls import path
from . import views

urlpatterns = [
    path('website-brief/', views.website_brief, name='website_brief'),
    path('thank-you/', views.thank_you, name='thank_you'),
]