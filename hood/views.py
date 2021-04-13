from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from .models import *
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import action, permission_classes as permission_decorator
from rest_framework.permissions import AllowAny

from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


def home(request):
    hood = Neighbourhood.objects.all()
    business = Business.objects.all()
    posts = Post.objects.all()
    # print("Results..", posts)
    heading = "Welcome to Neighborhood application"
    return render(request, "home.html", {"hoods":hood, "business":business,"posts":posts, "heading":heading})

class NeighbourhoodViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing neighborhood instances.
    """
    serializer_class = NeighbourhoodSerializer
    queryset = Neighbourhood.objects.all()
    
class ProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
class BusinessViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class IsAssigned(permissions.BasePermission): 
    """
    Only person who is assigned has the permission
    """
    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        if obj.assigned_to == request.user: 
            return True
        return False

class IsReadOnlyOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        authenticated = request.user.is_authenticated
        if not authenticated:
            if view.action == '/':
                return True
            else:
                return False
        else:
            return True

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = permissions.IsAuthenticated