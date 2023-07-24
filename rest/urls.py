from django.urls import path, include
from rest.views.task import TaskList, TaskSingle, TaskCreate, TaskDelete, TaskUpdate, TaskManaged
from rest.views.manager import ManagerList
from rest.views.user import UserList, UserCreate, UserDelete, UserUpdate
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('get_list_task/', TaskList.as_view()),
    path('get_single_task/<pk>/', TaskSingle.as_view()),
    path('create_task/', TaskCreate.as_view()),
    path('delete_task/<pk>/', TaskDelete.as_view()),
    path('update_task/<pk>/', TaskUpdate.as_view()),
    path('get_list_user/', UserList.as_view()),
    path('create_user/', UserCreate.as_view()),
    path('delete_user/<pk>/', UserDelete.as_view()),
    path('update_user/<pk>/', UserUpdate.as_view()),
    path('get_list_manager/', ManagerList.as_view()),
    path('get_managed_tasks/<pk>/', TaskManaged.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]