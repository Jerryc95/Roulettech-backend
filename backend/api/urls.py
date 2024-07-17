from django.urls import path
from .views import get_campaigns

urlpatterns = [
    path('campaigns/', get_campaigns, name='get_campaigns'),
]