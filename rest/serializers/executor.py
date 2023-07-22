from rest_framework import serializers
from users.models import Executor

class ExecutorSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    class Meta:
        model = Executor
        fields = '__all__'
        
    def get_username(self, obj):
        return obj.user.username
        