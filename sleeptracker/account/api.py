from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token

#Register API
class RegisterAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user, context=self.get_serializer_context()).data})

# Login API
class LoginAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):

        #token_created is just a placeholder to handle the boolean value created in the tuple
        login_serializer = self.get_serializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        user_object = login_serializer.validated_data
        user_token, token_created = Token.objects.get_or_create(user=user_object)
        return Response({
            "User": UserSerializer(user_object, context=self.get_serializer_context()).data,
            "Token": user_token.key
        })

# Get User Api

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
