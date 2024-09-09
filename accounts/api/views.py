from rest_framework import mixins, generics
from rest_framework.views import APIView
from .serializers import SignUpSerializer,UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from datetime import timedelta,datetime
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class SignUpView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_class = [IsAuthenticated]   
    def post(self,request):
        logout(request)
        return Response({'message': 'Logged out successfully!'}, status=status.HTTP_200_OK)


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user  

        if not check_password(data['current_password'], user.password):
            return Response({'message': 'The current password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        if data['new_password'] != data['confirm_new_password']:
            return Response({'message': 'The new password does not match the confirm new password'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(data['new_password'])
        user.save()

        return Response({'message': 'Password changed successfully!'}, status=status.HTTP_200_OK)

class ForgotPassword(APIView):
    def post(self, request):
        data = request.data 
        user = get_object_or_404(User,username=data['username'])

        # genarate a token 
        token = get_random_string(40)
        # set the token validity period to 30 minutes from now.
        expire_data = datetime.now() + timedelta(minutes=30)
        
        # save token,expire_data in profile 
        user.profile.reset_password_token = token 
        user.profile.reset_password_expire = expire_data
        user.profile.save()
        
        link = 'http://localhost:8000/accounts/api/reset-password/{token}/'.format(token=token)
        message = 'Your password reset link is : {link}'.format(link=link)
        subject = "password resert from JobBoard "
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [data['email']]
        )
        return Response({'details':'password reset sent to {email}'.format(email=data['email'])})


class ResetPassword(APIView):
   
    def post(self, request,token):
        data = request.data 
        user = get_object_or_404(User,profile__reset_password_token = token )

        if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now() :
            return Response({'Error':'Token is expire'},status=status.HTTP_400_BAD_REQUEST)

        if data['password'] != data['confirmpassword'] :
            return Response({'Error':'Password are not same'},status=status.HTTP_400_BAD_REQUEST)
            
        # Update password 
        user.password = make_password(data['password'])

        # Deleted becuse password is changed 
        user.profile.reset_password_token = ""
        user.profile.reset_password_expire = None
        
        user.profile.save()
        user.save()
        
        
        return Response({'details':'Password reset Sucessfully.. '})

class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({'profile':serializer.data})
    
    def put(self,request):
        user = request.user 
        data = request.data 
        
        # Update 
        user.first_name = data['first_name'] 
        user.last_name = data['last_name'] 
        user.username = data['username'] 
        user.email = data['email']    

        user.save()
        serializer = UserSerializer(user,many=False) 
                
        return Response(serializer.data, status=status.HTTP_201_CREATED)

  
