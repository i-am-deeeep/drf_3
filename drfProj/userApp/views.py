from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "User logged out successfully."}, status=200)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=400)

class RegistrationView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data={'response':'User created!'}
            user=serializer.save()
            data['username']=user.username
            data['email']=user.email

            refresh=RefreshToken.for_user(user)
            data['refresh-token']=str(refresh)
            data['access-token']=str(refresh.access_token)
            return Response(data)
        return Response(serializer.errors)
