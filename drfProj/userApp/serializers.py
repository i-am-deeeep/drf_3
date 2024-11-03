from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True, style={'input_type':'password'})
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={'password':{
            'write_only':True
        }}

    def validate_email(self,value):
        qset=User.objects.filter(email=value)
        if qset.exists():
            raise serializers.ValidationError({'error':'Email already in use'})
        else:
            return value
        
    def save(self):
        if self.validated_data['password']!=self.validated_data['password2']:
            raise serializers.ValidationError({'errors':"p1 and p2 do not match"})
        user_instance=User(username=self.validated_data['username'],email=self.validated_data['email'])
        user_instance.set_password(self.validated_data['password'])
        user_instance.save()
        return user_instance