from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from users.models import UserProfile
from .serializers import UserProfileSerializer

from . import permissions

# class UserListView(ListAPIView):
#       queryset = UserProfile.objects.all()
#       serializer_class = UserProfileSerializer

# class UserListView(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = UserProfile.objects.all()
#         serializer = UserProfileSerializer(queryset, many=True)
#         return Response(serializer.data)

class UserListView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnProfile,)
