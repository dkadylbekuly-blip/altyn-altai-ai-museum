import base64
import uuid

from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from telegram_bot.ml.predict import predict_image
from telegram_bot.services.mineral_lookup import get_mineral_card

from .models import RecognitionHistory, FavoriteMineral
from .serializers import RecognitionHistorySerializer


def get_site_user_id(request):
    return request.user.id if request.user.is_authenticated else 0


def save_and_predict_by_path(request, saved_path):
    full_path = default_storage.path(saved_path)
    prediction = predict_image(full_path)

    lang = getattr(request, "LANGUAGE_CODE", "ru")
    info = get_mineral_card(prediction["name"], lang)

    user_id = get_site_user_id(request)

    RecognitionHistory.objects.create(
        user_id=user_id,
        mineral_name=prediction["name"],
        confidence=prediction["confidence"],
        image=saved_path
    )

    is_favorite = FavoriteMineral.objects.filter(
        user_id=user_id,
        mineral_name=prediction["name"]
    ).exists()

    return {
        "name": prediction["name"],
        "confidence": prediction["confidence"],
        "top3": prediction.get("top3", []),
        "image_url": default_storage.url(saved_path),
        "info": info,
        "is_favorite": is_favorite,
    }


def upload_page(request):
    result = None
    error = None

    if request.method == "POST":
        image = request.FILES.get("image")

        if not image:
            error = "Файл не выбран."
        else:
            try:
                saved_path = default_storage.save(
                    f"recognitions/{uuid.uuid4()}.jpg",
                    ContentFile(image.read())
                )

                result = save_and_predict_by_path(request, saved_path)

            except Exception as e:
                error = str(e)

    return render(request, "recognize/upload.html", {
        "result": result,
        "error": error,
    })


def camera_page(request):
    result = None
    error = None

    if request.method == "POST":
        camera_image = request.POST.get("camera_image")

        if not camera_image:
            error = "Снимок с камеры не получен."
        else:
            try:
                _, imgstr = camera_image.split(";base64,")
                image_data = base64.b64decode(imgstr)

                image_file = ContentFile(image_data, name=f"{uuid.uuid4()}.jpg")

                saved_path = default_storage.save(
                    f"recognitions/{image_file.name}",
                    image_file
                )

                result = save_and_predict_by_path(request, saved_path)

            except Exception as e:
                error = str(e)

    return render(request, "recognize/camera.html", {
        "result": result,
        "error": error,
    })


def history_page(request):
    recognitions = RecognitionHistory.objects.all().order_by("-created_at")

    return render(request, "recognize/history.html", {
        "recognitions": recognitions
    })


def add_favorite(request, mineral_name):
    user_id = get_site_user_id(request)

    FavoriteMineral.objects.get_or_create(
        user_id=user_id,
        mineral_name=mineral_name
    )

    return redirect(f"/{getattr(request, 'LANGUAGE_CODE', 'ru')}/recognize/favorites/")


def remove_favorite(request, mineral_name):
    user_id = get_site_user_id(request)

    FavoriteMineral.objects.filter(
        user_id=user_id,
        mineral_name=mineral_name
    ).delete()

    return redirect(f"/{getattr(request, 'LANGUAGE_CODE', 'ru')}/recognize/favorites/")


def favorites_page(request):
    lang = getattr(request, "LANGUAGE_CODE", "ru")
    user_id = get_site_user_id(request)

    favorites = FavoriteMineral.objects.filter(user_id=user_id)

    cards = []

    for favorite in favorites:
        info = get_mineral_card(favorite.mineral_name, lang)

        cards.append({
            "name": favorite.mineral_name,
            "info": info,
            "created_at": favorite.created_at,
        })

    return render(request, "recognize/favorites.html", {
        "favorites": cards
    })


@api_view(["POST"])
def save_recognition(request):
    serializer = RecognitionHistorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Recognition saved"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)