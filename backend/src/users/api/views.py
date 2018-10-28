from rest_framework.generics import ListAPIView, RetrieveAPIView

from users.models import UserProfile
from .serializers import UserProfileSerializer

class UserListView(ListAPIView):
      queryset = UserProfile.objects.all()
      serializer_class = UserProfileSerializer

class UserDetailView(RetrieveAPIView):
      queryset = UserProfile.objects.all()
      serializer_class = UserProfileSerializer
