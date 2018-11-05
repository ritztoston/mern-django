from django.utils import timezone
from django.conf import settings
import datetime
from rest_framework_jwt.settings import api_settings


expires_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.id,
      	'expires': timezone.now() + expires_delta - datetime.timedelta(seconds=300)
    }
