from django.urls import path

from users.views import AuthCreateUserView, TokenCreateView

app_name = 'users'

urlpatterns = [
    path('signup/', AuthCreateUserView.as_view(), name='signup'),
    path('token/', TokenCreateView.as_view(), name='token'),
]
