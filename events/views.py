from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Event, RSVP, Review, InvitedUser
from .serializers import EventSerializer, RSVPSerializer, ReviewSerializer, InvitedUserSerializer
from .permissions import IsOrganizerOrReadOnly, IsInvitedUserOrPublic, Organizeraccessinviteduser
from rest_framework import filters

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOrganizerOrReadOnly, IsInvitedUserOrPublic]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location', 'organizer__username']

    def get_queryset(self):
        if self.request.method == 'GET' and 'public' in self.request.query_params:
            return Event.objects.filter(is_public=True)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post', 'patch'])
    def rsvp(self, request, pk=None):
        event = self.get_object()
        user = request.user
        rsvp_status = request.data.get('status')
        rsvp, created = RSVP.objects.get_or_create(event=event, user=user)
        rsvp.status = rsvp_status
        rsvp.save()
        return Response({'status': rsvp_status})

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Review.objects.filter(event_id=event_id)

    def perform_create(self, serializer):
        event_id = self.kwargs['event_id']
        event = get_object_or_404(Event, pk=event_id)
        serializer.save(user=self.request.user, event=event)

class InvitedUserSet(viewsets.ModelViewSet):
    queryset = InvitedUser.objects.all()
    serializer_class = InvitedUserSerializer
    permission_classes = [Organizeraccessinviteduser]

    def create(self, request, *args, **kwargs):
        event_id = self.kwargs['event_id']
        event = get_object_or_404(Event, pk=event_id)

        return super().create(request, *args, **kwargs)



        



