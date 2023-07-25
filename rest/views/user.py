from rest_framework import generics
from users.models import User
from rest.serializers.user import   (UserSerializer,
                                    UserCreateSerializer,
                                    UserUpdateAsExecutor)
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest.permissions import    (IsManagerUser,
                                IsSelfUserOrReadOnly,
                                IsTaskExecutorOrReadOnly)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ('username', 'id')
    permission_classes = [IsAuthenticated]
    
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
class UserDelete(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdminUser]
    
class UserUpdateAsExecutor(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateAsExecutor
    permission_classes = [IsSelfUserOrReadOnly]