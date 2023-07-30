from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from .models import CustomUser, Profile


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=11)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password_confirm')

    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     password_confirm = attrs.get('password_confirm')
    #
    #     if password != password_confirm:
    #         raise AuthenticationFailed('The entered passwords do not match')
    #
    #     return attrs
    #
    # def create(self, validated_data):
    #     email = validated_data.get('email')
    #     password = validated_data.get('password')
    #     user = CustomUser.objects.create(email=email)
    #     user.set_password(password)
    #     user.save()
    #     return user

    # def create(self, validated_data):
    #     password_confirm = validated_data.pop('password_confirm', None)
    #     if password_confirm is not None:
    #         if validated_data['password'] != password_confirm:
    #             raise AuthenticationFailed('The entered passwords do not match')
    #
    #     return CustomUser.objects.create(**validated_data)


class AuthUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Token
        fields = ('email', 'password', 'created')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
