from django.urls import path, include
urlpatterns = [
    path('', include('app_number_game.urls')),
]