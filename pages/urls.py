from django.urls import path
from django.shortcuts import redirect
from . import views


app_name = "pages"


def redirect_to_recognition_history(request):
    lang = getattr(request, "LANGUAGE_CODE", None) or "ru"
    return redirect(f"/{lang}/recognize/history/")


urlpatterns = [
    path("", views.home, name="home"),

    path("about/", views.about, name="about"),
    path("collection/", views.collection, name="collection"),
    path("gallery/", views.gallery, name="gallery"),

    # временные заглушки
    path("tours/", views.home, name="tours"),
    path("statistics/", views.home, name="statistics"),
    path("map/", views.home, name="map"),

    path("history/", redirect_to_recognition_history, name="history"),

    path(
        "mineral/<slug:slug>/",
        views.mineral_detail,
        name="mineral_detail"
    ),
]