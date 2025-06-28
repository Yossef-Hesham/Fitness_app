from django.urls import path
from .views import *

# your_view = ProfileView.as_view({
#     'get': 'list',   # Dictionary with key-value pairs
#     'post': 'create'
# })

urlpatterns = [
    path('user/register/', UserRegisterView.as_view()),
    path('user/login/', UserloginView.as_view()),
]