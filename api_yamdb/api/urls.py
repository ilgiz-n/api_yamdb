from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet


router_v1 = DefaultRouter()
router_v1.register(r'categories', CategoriesViewSet, basename='categories')
router_v1.register(r'genres', GenresViewSet, basename='genres')
router_v1.register(r'titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
