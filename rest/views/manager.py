from rest_framework import generics
from rest_framework import permissions
from users.models import Manager
from rest.serializers.manager import ManagerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ManagerList(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('username', 'id')

# class ManagedTasks(generics.RetrieveAPIView):
#     queryset = Manager.managed_tasks.all()
#     serializer_class = ManagerSerializer

# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
