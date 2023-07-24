from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer,
    UserDeleteSerializer as BaseUserDeleteSerializer,
)


# Custom UserCreateSerializer
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", "first_name", "last_name"]


# Custom UserSerializer
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]


# Custom UserDeleteSerializer
class UserDeleteSerializer(BaseUserDeleteSerializer):
    class Meta(BaseUserDeleteSerializer.Meta):
        # Add any custom fields or configurations if needed
        pass
