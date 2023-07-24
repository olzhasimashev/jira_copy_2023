from rest_framework import generics
from rest_framework import permissions
from tasks.models import Task
from rest.serializers.task import TaskSerializer, TaskCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest.permissions import IsExecutorUser, IsManagerUser
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('name', 'id')
    permission_classes = [IsAuthenticated]
    
class TaskSingle(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = [IsManagerUser]
    
    def create(self, request, *args, **kwargs):
        input_deadline = request.data.get('deadline')
        if input_deadline:
            parsed_deadline = datetime.strptime(input_deadline, '%a %b %d %Y %H:%M:%S %Z%z')
            request.data['deadline'] = parsed_deadline.strftime('%Y-%m-%dT%H:%M:%SZ')

        return super().create(request, *args, **kwargs)
    
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