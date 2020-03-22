"""heimspiel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from heimspiel_auth import views as auth_views
from heimspiel_core import views

router = routers.DefaultRouter()
router.register(r'badges', views.BadgeViewSet)
router.register(r'playerattributes', views.PlayerAttributeViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'questcategories', views.QuestCategoryViewSet)
router.register(r'quests', views.QuestViewSet)
router.register(r'users', auth_views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('scorereports/', views.score_reports),
] + static('media/', document_root=settings.MEDIA_ROOT)
