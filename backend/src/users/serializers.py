from rest_framework import serializers
from users.models import UserProfile
from rest_framework.response import Response

from .settings.helpers import letters_and_num_only, letters_only

import os
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

class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, max_length=255, write_only=True, allow_null=True, allow_blank=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, max_length=255, write_only=True, allow_null=True, allow_blank=True)
    isReadyCreateUser = serializers.BooleanField(default=False)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'url', 'username', 'email', 'firstname', 'lastname', 'avatar','password', 'password2', 'isReadyCreateUser', 'token', 'expires')

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')
        if pw == '':
            raise serializers.ValidationError({'password': 'Password is required.'})
        if pw != pw2:
            raise serializers.ValidationError({'password': 'Password must match.', 'password2': 'Password must match.'})

        return data

    def validate_username(self, value):
        if not letters_only(value):
            raise serializers.ValidationError('Only letters are allowed.')
        if len(value) == 0 or value is None or value == '':
            raise serializers.ValidationError('Username is required.')
        if len(value) < 5 or len(value) > 11:
            raise serializers.ValidationError('Minimum of 5 or maximum of 11 characters only.')
        return value

    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('Email is required.')
        return value

    def validate_firstname(self, value):
        if not letters_only(value):
            raise serializers.ValidationError('Only letters are allowed')
        if len(value) == 0 or value is None or value == '':
            raise serializers.ValidationError('First Name is required.')
        return value

    def validate_lastname(self, value):
        if not letters_only(value):
            raise serializers.ValidationError('Only letters are allowed')
        if len(value) == 0 or value is None or value == '':
            raise serializers.ValidationError('Last Name is required.')
        return value

    def validate_password(self, value):
        if len(value) == 0 or value is None or value == '':
            raise serializers.ValidationError('Password is required.')
        if len(value) < 4 or len(value) > 11:
            raise serializers.ValidationError('Minimum of 4 or maximum of 11 characters only.')
        return value

    def validate_password2(self, value):
        if len(value) == 0 or value is None or value == '':
            raise serializers.ValidationError('Confirm password is required.')
        return value

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return timezone.now() + expires_delta - datetime.timedelta(seconds=1)

    def create(self, validated_data):
        print(validated_data)

        if validated_data['isReadyCreateUser']:
            avatar = ''
            if validated_data.get('avatar') == None:
                avatar = 'default/' + os.path.basename(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'media', 'default', 'no-image.png'))
            else:
                avatar = validated_data['avatar']

            user = UserProfile(
                email = validated_data['email'],
                username = validated_data['username'],
                firstname = validated_data['firstname'],
                lastname = validated_data['lastname'],
                avatar = avatar
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
