from rest_framework import serializers
from users.models import Manager

class ManagerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    class Meta:
        model = Manager
        fields = '__all__'
        
    def get_username(self, obj):
        return obj.user.username
        
# class UserCreateSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'is_manager', 'is_executor')