from .models import (
    Activity, 
    Schedule, 
    Workout, 
    Friend, 
    Photo, 
    Message
)
from django.contrib.auth.models import User
from rest_framework import (
    viewsets, 
    permissions, 
    mixins
)
from .serializers import (
    ActivitySerializer, 
    ScheduleSerializer, 
    WorkoutSerializer, 
    UserSerializer, 
    FriendSerializer, 
    PhotoSerializer, 
    MessageSerializer
)

class ActivityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Activity.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ActivitySerializer

class ScheduleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Schedule.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScheduleSerializer

class ScheduleCRUDViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return self.request.user.schedules.all()

class WorkoutViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Workout.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = WorkoutSerializer

class WorkoutCRUDViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return self.request.user.workouts.all()

        

class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.filter(is_superuser=False)
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = UserSerializer

class FollowerViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FriendSerializer

    def get_queryset(self):
        return self.request.user.following.all()

class FriendViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Friend.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = FriendSerializer

class PhotoCRUDViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class =PhotoSerializer

    def get_queryset(self):
        return self.request.user.photo.all()

class PhotoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Photo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = PhotoSerializer

class IncomingMessageCRUDViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MessageSerializer

    def get_queryset(self):
        return self.request.user.incoming.all()

class OutoingMessageCRUDViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MessageSerializer

    def get_queryset(self):
        return self.request.user.outgoing.all()
