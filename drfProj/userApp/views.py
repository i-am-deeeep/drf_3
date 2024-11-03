from django.shortcuts import render
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['POST',])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response({'response':'Successfully logged out(deleted token)'})

@api_view(['POST',])
def register_view(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data={'response':'Registration Successful!!'}
            user_obj=serializer.save()
            Token.objects.get_or_create(user=user_obj)
            token=Token.objects.get(user=user_obj)
            data['username']=user_obj.username
            data['email']=user_obj.email
            data['password']=user_obj.password
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)