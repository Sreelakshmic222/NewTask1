from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
class RegisterAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'
    def get(self, request):
        # Your view logic here
        return Response({'message':'homepage'})
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Please provide username, email and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # generate JWT token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({'token': token}, status=status.HTTP_201_CREATED)




class LoginAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    def get(self, request):
        # Your view logic here
        return Response({'message':'homepage'})

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # generate JWT token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({'token': token}, status=status.HTTP_200_OK)


# def register(request):
#     if request.method == 'POST':
#         # handle registration form submission
#         ...
#     else:
#         # render registration form template
#         return render(request, 'register.html')


# def login(request):
#     if request.method == 'POST':
#         # handle login form submission
#         ...
#     else:
#         # render login form template
#         return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # redirect to success page
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             # authenticate user and redirect to success page
#             pass
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

class HomePageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'

    def get(self, request):
        # Your view logic here
        return Response({'message':'homepage'})

class IndexPageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def post(self, request):
        the_user = request.user
        # Your view logic here
        return Response({'Hai':'the_user'})