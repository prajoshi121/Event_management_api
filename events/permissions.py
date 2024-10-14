from rest_framework import permissions

class IsOrganizerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.organizer == request.user

class IsInvitedUserOrPublic(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_public:
            return True
        return request.user in obj.invited_users.all() or obj.organizer == request.user

class Organizeraccessiviteduser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.event.organizer:
            return True
        return False