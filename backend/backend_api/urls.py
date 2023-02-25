from backend_api.views import MovieViewSet
from rest_framework.routers import DefaultRouter
from backend_api import views
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
urlpatterns = router.urls
