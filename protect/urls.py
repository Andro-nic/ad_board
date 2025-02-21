from django.urls import path
from .views import IndexView
#from board.views import UserResponsesView

urlpatterns = [
    path('', IndexView.as_view()), #path('user/', IndexView.as_view(), name='user_index')
]