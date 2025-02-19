from django.urls import path
from .views import *

# your_view = ProfileView.as_view({
#     'get': 'list',   # Dictionary with key-value pairs
#     'post': 'create'
# })

urlpatterns = [
    path('user/profiles/', ProfileView.as_view({'get':'list'})),
    path('user/register/', RegisterView.as_view()),
    path('user/login/', LoginView.as_view()),
]