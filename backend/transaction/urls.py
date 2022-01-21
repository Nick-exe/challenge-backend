from django.urls import path

from transaction.views import get_transactions
from transaction.views import cancel_transaction

urlpatterns = [
    path('get-transactions/', get_transactions),
    path('cancel-transaction/', cancel_transaction),
]
