from rest_framework import viewsets, filters
from .serializers import DataSerializer, StarRatingSerializer, DataTAVSerializer
from .models import Data, StarRating, DataTAV


# Create your views here.
class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all().order_by('-fecha')
    serializer_class = DataSerializer


class StarRatingViewSet(viewsets.ModelViewSet):
    queryset = StarRating.objects.all()
    serializer_class = StarRatingSerializer


class DataTAVViewset(viewsets.ModelViewSet):
    search_fields = ['run']
    filter_backends = (filters.SearchFilter,)
    queryset = DataTAV.objects.all()
    serializer_class = DataTAVSerializer


# class DataTAVViewset(generics.ListCreateAPIView):
#     queryset = DataTAV.objects.all()
#     serializer_class = DataTAVSerializer

# class DataTAVViewset(generics.ListCreateAPIView):
#     search_fields = ['run']
#     filter_backends = (filters.SearchFilter,)
#     queryset = DataTAV.objects.all()
#     serializer_class = DataTAVSerializer
