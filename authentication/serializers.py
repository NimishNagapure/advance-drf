from django.contrib.auth import tokens
from django.db import models
from django.db.models import fields
from rest_framework import serializers, status
from rest_framework_simplejwt.tokens import Token

from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class RegisterSerializer(serializers.ModelSerializer):  
    password = serializers.CharField(
        max_length=255, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', ' ')
        username = attrs.get('username', ' ')


        if not username.isalnum():
            raise serializers.ValidationError(
                'The Username should only contain alphanumeric alphanumeric')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(
    max_length=70, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=6, read_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens', 'username']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        filtered_user_by_email = User.objects.filter(email=email)


        user = auth.authenticate(email=email, password=password)
        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider !='email':
            raise AuthenticationFailed(detail='Please continue your login using' + filtered_user_by_email[0].auth_provider)
        if not user:
            raise AuthenticationFailed('Invalid Credentials')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is Not Verified')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.tokens()
        }
        return super().validate(attrs)


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=6)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68,write_only=True)
    uidb64 = serializers.CharField(min_length=1,write_only=True)
    token = serializers.CharField(min_length=6,write_only=True)

    class Meta:
        fields = ['password', 'uidb64', 'token']

    def validate(self, attrs):
        try:
            password = attrs.get('password', '')
            token = attrs.get('token', '')
            uidb64 = attrs.get('uidb64', '')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The rest link is invalid',status=status.HTTP_401_UNAUTHORIZED)  

            user.set_password(password)
            user.save()
            return (user)

        except Exception as e:
            raise AuthenticationFailed('The rest link is invalid',status=status.HTTP_401_UNAUTHORIZED)
        
        return super().validate(attrs)

            



