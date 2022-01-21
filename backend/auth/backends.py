import requests
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class CustomChallengeBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Creates user in backend if user is valid
            endpoint = 'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/user/login'
            payload = {
                'Username': username,
                'Password': password,
            }
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()

            user = User(username=username, password=password)
            user.save()
        return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
