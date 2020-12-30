from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser,CustomUserProfile
from users.serializers import CustomUserSerializer,CustomUserProfileSerializer


# @permission_classes([IsAuthenticated])
from rest_framework.viewsets import ModelViewSet


class CustomUserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    #
    # def list(self, request, *args, **kwargs):
    #     raise PermissionDenied()

    def list(self, request, *args, **kwargs):
        queryset = get_user_model().objects.all()
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data)


# @permission_classes([IsAuthenticated])
class CustomUserProfileView(APIView):
    def get(self, request, pk):
        profile = CustomUserProfile.objects.get(user=pk)
        serializer = CustomUserProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request, pk):
        # name, bio, github_username, avatar, current_level
        profile = CustomUserProfile(**request.data)
        profile.user = get_user_model().objects.get(pk=pk)
        profile.save()

        return Response('Success')
