from django.contrib.auth import authenticate

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token


from .models import Usuario
from .serializers import UsuarioSerializer, LoginSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid() is False:
            return Response(serializer.errors, status=400)

        authenticated_user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if authenticated_user is None:
            return Response({"error": "Invalid credentials"}, status=400)

        token, create = Token.objects.get_or_create(user=authenticated_user)

        return Response(
            {"token": token.key, "user": self.get_serializer(authenticated_user).data},
            status=200,
        )
