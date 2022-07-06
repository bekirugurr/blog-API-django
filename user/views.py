from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .models import Profile
from .serializers import RegisterSerializer, UserSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import IsCurrentUserOwnerOrAdminOrReadOnlyForProfile,IsCurrentUserOwnerOrAdminOrReadOnlyForUser




#! Her register işleminde token üretsin diye create methodunu override ettim
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        user = serializer.save()
        token = Token.objects.create(user=user)
        data = serializer.data
        data['token'] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class GetUpdateUserView(RetrieveUpdateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    permission_classes= (IsCurrentUserOwnerOrAdminOrReadOnlyForUser,)

class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes= (IsCurrentUserOwnerOrAdminOrReadOnlyForProfile,)




