from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import exceptions, mixins, permissions, viewsets
from tasks.models import User
from tasks.serializers import UserSerializer 
# Create your views here.

class UserViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet,):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(id = self.request.user.id)

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny(),]
        else:
            return [permissions.IsAuthenticated(),]

    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        if obj != request.user:
            raise exceptions.PermissionDenied("アーカイブ済みのTodoは操作できません。")