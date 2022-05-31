from django.conf import settings
from rest_framework import permissions


class JwtAuth(permissions.BasePermission):
    """Права доступа по JWT токену"""

    def has_permission(self, request, view):
        """Устанавливает общие права на доступ"""
        token = request.headers.get("Authorization")
        if token:
            token = token.split(' ')[-1]
        return token == settings.JWT_TOKEN
