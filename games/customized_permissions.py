from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #if GET, POST, PATCH
            return True
        else:
            return obj.owner == request.user #if it's the owner