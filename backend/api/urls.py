from django.urls import path
from . import views
from .views import get_campaigns

urlpatterns = [
    # path("", views.index, name="index"),
    path('campaigns/', get_campaigns, name='get_campaigns'),
    # path('campaigns/add/', add_campaign, name='add_campaign'),
    
]