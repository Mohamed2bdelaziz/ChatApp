from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChatViewSet, MessageViewSet, register, login_view

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('', include(router.urls)),
]