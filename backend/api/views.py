from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from .models import Campaign
from .serializers import CampaignSerializer

import logging

logger = logging.getLogger(__name__)

# Create your views here.
# def index(request):  
#     return HttpResponse("Hello, world.")

@api_view(['GET', 'POST', 'DELETE'])
def get_campaigns(request):
    if request.method == 'GET': 
        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        Campaign.objects.all().delete()
        return JsonResponse({'message': 'campaigns were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



