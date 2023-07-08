
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import rest_framework as drf_filters, CharFilter
from rest_framework_api.permissions import IsOwnerOrReadOnly
from .models import Poem
from .serializers import PoemSerializer


class PoemList(generics.ListCreateAPIView):
    """
    List poems or create a poem if logged in.
    """
    serializer_class = PoemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Poem.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filter_class = PoemFilter
    filterset_fields = {
        'owner__followed__owner__profile': ['exact'],
        'likes__owner__profile': ['exact'],
        'owner__profile': ['exact'],
        'published_at': ['date__gte', 'date__lte'],
        'category': ['exact'],
    }
    search_fields = (
        'owner__profile_name',
        'title',
        'created_at'
    )
    ordering_fields = (
        'likes_count',
        'comments_count',
        'likes__created_at',
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)          


class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a poem, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PoemSerializer
    queryset = Poem.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
