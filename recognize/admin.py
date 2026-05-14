from django.contrib import admin
from .models import RecognitionHistory, FavoriteMineral


@admin.register(RecognitionHistory)
class RecognitionHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "mineral_name", "confidence", "created_at")
    search_fields = ("mineral_name", "user_id")
    list_filter = ("created_at", "mineral_name")
    ordering = ("-created_at",)


@admin.register(FavoriteMineral)
class FavoriteMineralAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "mineral_name", "created_at")
    search_fields = ("mineral_name", "user_id")
    list_filter = ("created_at", "mineral_name")
    ordering = ("-created_at",)