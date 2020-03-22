from django.urls import path

from heimspiel_core import views

urlpatterns = [
    path('api/player/<str:pk>/', views.GetPlayer.as_view(), name='get_player'),
]
