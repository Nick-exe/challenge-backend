
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_401_UNAUTHORIZED

def err_invalid_credentials():
    return 'Invalid Credentials'


def err_bad_request():
    return 'User not authorized'

def err_login_required():
    return 'User is not logged in'


# @csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None:
        return Response({'error': err_bad_request()}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user:
        auth_login(request, user)
        return Response({'ok': True}, status=HTTP_200_OK)
    return Response({'error': err_invalid_credentials()}, status=HTTP_404_NOT_FOUND)


# @csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def logout(request):
    auth_logout(request)

# @csrf_exempt
@api_view(['POST', 'GET'])
@permission_classes((AllowAny,))
# @permission_classes((AllowAny,))
def login_required(request):
    return Response({'error': err_login_required()}, status=HTTP_401_UNAUTHORIZED)

