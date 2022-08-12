from rest_framework import permissions


class AdminModeratorAuthorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or obj.author == request.user)


class AdminSuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and (
                    request.user.is_admin or request.user.is_superuser)))


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.method in permissions.SAFE_METHODS)
                or (request.user
                    and request.user.is_authenticated
                    and request.user.role == 'admin'
                    )
                )
