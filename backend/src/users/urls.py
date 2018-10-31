from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('register', views.UserRegisterView)
router.register('users', views.UserListView)


urlpatterns = [
    path('users/register/', views.UserRegisterView.as_view()),
    path('', include(router.urls)),
]
