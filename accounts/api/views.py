from rest_framework import mixins, generics
from rest_framework.views import APIView
from .serializers import SignUpSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.response import Response
from rest_framework import status


class SignUpView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)