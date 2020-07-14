from rest_framework import serializers, filters
# Models
from .models import Data, StarRating, DataTAV


class StarRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarRating
        fields = ['id', 'run', 'rating_value']


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['run', 'nombre', 'exam', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'proctor', 'sede']


class DataTAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTAV
        fields = ['id', 'run', 'nombre', 'asignatura', 'seccion', 'fecha', 'hora_inicio', 'hora_fin', 'sala', 'docente']

