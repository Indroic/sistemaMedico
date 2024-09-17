from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'date_joined']
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    
    password = serializers.CharField()
    