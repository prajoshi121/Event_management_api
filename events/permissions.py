from rest_framework import permissions
from .models import Event

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

class Organizeraccessinviteduser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        event_id = view.kwargs.get('event_id') or request.data.get('event')
        
        if not event_id:
            return False
        
        event = Event.objects.filter(id=event_id).first()

        if event and request.user == event.organizer:
            return True

        return False