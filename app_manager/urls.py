from django.urls import path

from commons.utils import support_method

from .views import (
    MessageApiView
)

urlpatterns = [
    path('', MessageApiView.as_view(support_method), name='message-list'),
]
