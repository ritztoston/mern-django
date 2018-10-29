from rest_framework import serializers
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'firstname', 'lastname', 'avatar', 'password')

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
        instance.username = validated_data['username']
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


# class UserRegisterSerializer(serializers.Serializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
