from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets, mixins, generics, permissions
from rest_framework.response import Response
from users.models import UserProfile
from .serializers import UserProfileSerializer, UserRegisterSerializer

from . import permissions as permission

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
    permission_classes = (permission.UpdateOwnProfile,)

class UserRegisterView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    queryset = UserProfile.objects.all()
    permission_classes = []

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
