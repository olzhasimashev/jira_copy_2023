from rest_framework import generics
from rest_framework import permissions
from tasks.models import Task
from rest.serializers.task import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('name', 'id')
    
class TaskSingle(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskDelete(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskManaged(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        manager_id = self.kwargs['pk']
        return Task.objects.filter(manager__id=manager_id)