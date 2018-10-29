from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', views.UserListView)
# router.register('register/', views.UserRegisterView, base_name='register')

urlpatterns = [
      # path('users/register/', UserRegisterView.as_view()),
      path('', include(router.urls)),
      # path('users/id/<pk>', UserDetailView.as_view()),
]
