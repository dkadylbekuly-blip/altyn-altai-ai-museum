from rest_framework import serializers
from .models import RecognitionHistory, FavoriteMineral


class RecognitionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognitionHistory
        fields = "__all__"


class FavoriteMineralSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMineral
        fields = "__all__"