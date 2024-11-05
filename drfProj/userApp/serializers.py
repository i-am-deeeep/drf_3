from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True, style={'input_style':'password'})
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{
                'write_only':True
            }
        }
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError({'error':'Email already exists!'})
        return value
    def save(self):
        if self.validated_data['password']!=self.validated_data['password2']:
            raise serializers.ValidationError({'error':'p1 and p2 must be same!'})
        user=User(username=self.validated_data['username'], email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user

