from rest_framework import serializers
from users.models import UserProfile
from rest_framework.response import Response

import datetime
from django.utils import timezone
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expires_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'url', 'username', 'email', 'firstname', 'lastname', 'avatar','password')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, max_length=255, required=True, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, max_length=255, required=True, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'firstname', 'lastname', 'avatar','password', 'password2', 'token', 'expires')

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return timezone.now() + expires_delta - datetime.timedelta(seconds=1)

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw != pw2:
            raise serializers.ValidationError('Password must match.')

        return data

    def create(self, validated_data):
        user = UserProfile(
            email = validated_data['email'],
            username = validated_data['username'],
            firstname = validated_data['firstname'],
            lastname = validated_data['lastname'],
            avatar = validated_data['avatar']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    # def update(self, instance, validated_data):
    #
    #     instance.email = validated_data['email']
    #     instance.username = validated_data['username']
    #     instance.firstname  = validated_data['firstname']
    #     instance.lastname  = validated_data['lastname']
    #     instance.avatar  = validated_data['avatar']
    #
    #     instance.set_password(validated_data['password'])
    #     instance.save()
    #
    #     return instance
