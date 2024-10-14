from django.urls import path
from .views import EventViewSet, ReviewViewSet, InvitedUserSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event-list-create'),
    path('events/<int:pk>/', EventViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='event-detail'),
    
    
    path('events/<int:pk>/rsvp/', EventViewSet.as_view({'post': 'rsvp'}), name='event-rsvp'),
    

    path('events/<int:event_id>/reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='event-reviews'),
    path('events/<int:event_id>/reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='event-review-detail'),


    path('events/<int:event_id>/inviteduser/', InvitedUserSet.as_view({'get': 'list', 'post' : 'create' }), name='event-invitedusercreate'),
    path('events/<int:event_id>/inviteduser/<int:pk>', InvitedUserSet.as_view({'get': 'retrieve', }), name='event-inviteduser'),
]
