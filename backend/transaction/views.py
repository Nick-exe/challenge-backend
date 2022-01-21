
import requests
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view


# init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("cancelled-transactions.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

#get transactions view
@csrf_exempt
@api_view(['GET'])
def get_transactions(request):
    endpoint = 'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/user/transactions'
    response = requests.get(endpoint)
    response.raise_for_status()
    result = response.json()

    return Response(result, status=HTTP_200_OK)

#cancel transactions view
@csrf_exempt
@api_view(['POST'])
def cancel_transaction(request):
    data = request.data
    user = request.data['user']['email']
    logger.info(f'Cancel request for user {user}')
    logger.info(data)

    return Response('ok', status=HTTP_200_OK)
