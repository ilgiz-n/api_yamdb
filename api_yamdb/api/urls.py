from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from api.views import CategoriesViewSet, GenresViewSet, TitlesViewSet, ReviewsViewSet, CommentsViewSet
from users.views import UsersViewSet
from users.views import AuthCreateUserView, TokenCreateView


router_v1 = DefaultRouter()
router_v1.register(r'users', UsersViewSet, basename='users')
router_v1.register(r'categories', CategoriesViewSet, basename='categories')
router_v1.register(r'genres', GenresViewSet, basename='genres')
router_v1.register(r'titles', TitlesViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewsViewSet,
    basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('users.urls', namespace='auth')),
    # path('v1/auth/signup/', AuthCreateUserView.as_view(), name='signup'),
    # path('v1/auth/token/', TokenCreateView.as_view(), name='token'),
]

