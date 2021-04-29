from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    """
    list:
        Return all todos with authenticated user

    retrieve:
        Return a todo instance.

    create:
        Create a new todo

    update:
        Update the todo

    partial_update:
        Update one or more fields on an existing todo.

    delete:
        Remove an existing todo.
    """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(active=True, user=self.request.user)
        return None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(operation_id="Return all todos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Return a todo instance")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Create a new todo")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Update one or more fields on an existing todo")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Update a todo")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Remove an existing todo")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
