from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    
    
    def validate_password(self, value: str) -> str:
        return make_password(value)
    
    class Meta:
        model = User
        fields = '__all__'
        
class UserCreateSerializer(serializers.ModelSerializer):
    
    
    def validate_password(self, value: str) -> str:
        return make_password(value)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_manager', 'is_executor')
        
class UserUpdateAsExecutor(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str:
        return make_password(value)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password') 