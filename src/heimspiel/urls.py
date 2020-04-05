from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers

from heimspiel_auth import views as auth_views
from heimspiel_core import views


schema_view = get_schema_view(
   openapi.Info(
      title="Heimspiel API",
      default_version='v1',
      description="This is the description of the Heimspiel API.",
      contact=openapi.Contact(email="leipzig@opentechschool.org"),
      license=openapi.License(name="AGPL-3.0"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


class APIRootView(routers.APIRootView):
    permission_classes = [permissions.AllowAny]


class DefaultRouter(routers.DefaultRouter):
    APIRootView = APIRootView


router = DefaultRouter()
router.register(r"badges", views.BadgeViewSet)
router.register(r"playerattributes", views.PlayerAttributeViewSet)
router.register(r"players", views.PlayerViewSet)
router.register(r"questcategories", views.QuestCategoryViewSet)
router.register(r"quests", views.QuestViewSet)
router.register(r"users", auth_views.UserViewSet)

urlpatterns = [
<<<<<<< 36ee870bb25455e00de55b81b763f71b8a40fce7
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("scorereports/", views.score_reports),
] + static("media/", document_root=settings.MEDIA_ROOT)
=======
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('scorereports/', views.score_reports),
] + static('media/', document_root=settings.MEDIA_ROOT)
>>>>>>> Add docs URL
