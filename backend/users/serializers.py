from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers

from .models import NewUser, UserProfile


class NewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = ("email", "user_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
            "eth_address",
            "payment_type",
            "total_no_of_nfts",
            "total_paid",
            "nft_ids",
        )


class PasswordRestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = ("email",)


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        field = ("password",)

    def validate(self, value):
        try:
            password = value.get("password")
            token = self.context.get("kwargs").get("token")
            encoded_pk = self.context.get("kwargs").get("encoded_pk")

            if token is None or encoded_pk is None:
                raise serializers.ValidationError("Missing token or encoded_pk")

            pk = urlsafe_base64_decode(encoded_pk).decode()
            user = NewUser.objects.get(pk=pk)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError(
                    "Rest token is not valid, please request a new one"
                )

            user.set_password(password)
            user.save()
            return value
        except Exception:
            raise serializers.ValidationError(
                "Something went wrong in reset token validation process"
            )
