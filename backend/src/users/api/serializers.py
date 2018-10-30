from rest_framework import serializers
from users.models import UserProfile
from rest_framework.response import Response


class UserProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, max_length=255, required=True, write_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'firstname', 'lastname', 'avatar', 'password', 'password2')


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

    def update(self, instance, validated_data):

        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.firstname  = validated_data['firstname']
        instance.lastname  = validated_data['lastname']
        instance.avatar  = validated_data['avatar']

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


# class UserRegisterSerializer(serializers.Serializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
