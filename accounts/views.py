from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from .permissions import UserPermission
from .serializers import UserAccountSerializer
from .models import UserAccount


class UserAccountView(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    serializer_class = UserAccountSerializer
    permission_classes = [UserPermission]

    def get_queryset(self):
        queryset = UserAccount.objects.all().select_related()
        return queryset

    @swagger_auto_schema(operation_id="Return all users")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Return a user instance")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Create a new user")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Update one or more fields on an existing user")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Update a user")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="Remove an existing user")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
