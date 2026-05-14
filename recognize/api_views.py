from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from telegram_bot.ml.predict import predict_image
from telegram_bot.services.mineral_lookup import get_mineral_card

from .models import RecognitionHistory, FavoriteMineral
from .serializers import RecognitionHistorySerializer, FavoriteMineralSerializer


@api_view(["POST"])
def mobile_recognize(request):
    image = request.FILES.get("image")
    user_id = request.data.get("user_id", 0)
    lang = request.data.get("lang", "ru")

    if not image:
        return Response(
            {"error": "Image file is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    saved_path = default_storage.save(
        f"recognitions/mobile_{image.name}",
        ContentFile(image.read())
    )

    full_path = default_storage.path(saved_path)
    prediction = predict_image(full_path)
    info = get_mineral_card(prediction["name"], lang)

    RecognitionHistory.objects.create(
        user_id=user_id,
        mineral_name=prediction["name"],
        confidence=prediction["confidence"],
        image=saved_path
    )

    return Response({
        "success": True,
        "result": {
            "name": prediction["name"],
            "confidence": prediction["confidence"],
            "top3": prediction.get("top3", []),
            "image_url": request.build_absolute_uri(default_storage.url(saved_path)),
            "info": info,
        }
    })


@api_view(["GET"])
def mobile_history(request):
    user_id = request.GET.get("user_id")

    queryset = RecognitionHistory.objects.all().order_by("-created_at")

    if user_id:
        queryset = queryset.filter(user_id=user_id)

    serializer = RecognitionHistorySerializer(queryset[:50], many=True)

    return Response({
        "success": True,
        "history": serializer.data
    })


@api_view(["GET"])
def mobile_mineral_info(request, mineral_name):
    lang = request.GET.get("lang", "ru")
    info = get_mineral_card(mineral_name, lang)

    return Response({
        "success": True,
        "mineral": mineral_name,
        "info": info
    })


@api_view(["GET"])
def mobile_favorites(request):
    user_id = request.GET.get("user_id", 0)

    favorites = FavoriteMineral.objects.filter(user_id=user_id).order_by("-created_at")
    serializer = FavoriteMineralSerializer(favorites, many=True)

    return Response({
        "success": True,
        "favorites": serializer.data
    })


@api_view(["POST"])
def mobile_add_favorite(request):
    user_id = request.data.get("user_id", 0)
    mineral_name = request.data.get("mineral_name")

    if not mineral_name:
        return Response(
            {"error": "mineral_name is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    favorite, created = FavoriteMineral.objects.get_or_create(
        user_id=user_id,
        mineral_name=mineral_name
    )

    return Response({
        "success": True,
        "created": created,
        "favorite": FavoriteMineralSerializer(favorite).data
    })


@api_view(["POST"])
def mobile_remove_favorite(request):
    user_id = request.data.get("user_id", 0)
    mineral_name = request.data.get("mineral_name")

    if not mineral_name:
        return Response(
            {"error": "mineral_name is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    deleted_count, _ = FavoriteMineral.objects.filter(
        user_id=user_id,
        mineral_name=mineral_name
    ).delete()

    return Response({
        "success": True,
        "deleted": deleted_count > 0
    })