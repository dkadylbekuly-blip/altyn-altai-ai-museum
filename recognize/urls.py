from django.urls import path
from . import views
from . import api_views

app_name = "recognize"

urlpatterns = [
    path("upload/", views.upload_page, name="upload"),
    path("camera/", views.camera_page, name="camera"),
    path("history/", views.history_page, name="history"),

    path("favorites/", views.favorites_page, name="favorites"),
    path("favorites/add/<str:mineral_name>/", views.add_favorite, name="add_favorite"),
    path("favorites/remove/<str:mineral_name>/", views.remove_favorite, name="remove_favorite"),

    path("save-recognition/", views.save_recognition, name="save_recognition"),

    path("mobile/recognize/", api_views.mobile_recognize, name="mobile_recognize"),
    path("mobile/history/", api_views.mobile_history, name="mobile_history"),
    path("mobile/mineral/<str:mineral_name>/", api_views.mobile_mineral_info, name="mobile_mineral_info"),
    path("mobile/favorites/", api_views.mobile_favorites, name="mobile_favorites"),
    path("mobile/favorites/add/", api_views.mobile_add_favorite, name="mobile_add_favorite"),
    path("mobile/favorites/remove/", api_views.mobile_remove_favorite, name="mobile_remove_favorite"),
]