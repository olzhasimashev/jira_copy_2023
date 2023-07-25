from rest_framework import serializers
from tasks.models import Task
from .executor import ExecutorSerializer
from .manager import ManagerSerializer

class TaskSerializer(serializers.ModelSerializer):
    executors = ExecutorSerializer(many=True)
    manager = ManagerSerializer()
    
    class Meta:
        model = Task
        fields = '__all__'
        
class TaskCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'
        
class TaskUpdateExecutorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['is_active']