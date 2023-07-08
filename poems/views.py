from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter
from django_filters import rest_framework as drf_filters
from .models import Poem
from .serializers import PoemSerializer


class PoemList(generics.ListCreateAPIView):
    """
    List poems or create a poem if logged in.
    """
    serializer_class = PoemSerializer
    queryset = Poem.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)   


class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a poem, or update or delete it by id if you own it.
    """
    serializer_class = PoemSerializer
    queryset = Poem.objects.all().order_by('-created_at')
