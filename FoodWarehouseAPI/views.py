from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from . serializers import fstockSerializer
from . models import fstock

class fstockviewset(viewsets.ModelViewSet):
    queryset = fstock.objects.all().order_by('Mfd_id')
    serializer_class = fstockSerializer
