from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.api.urls')),
    path('api/login/', obtain_jwt_token),
    path('api/auth/jwt/refresh/', refresh_jwt_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
