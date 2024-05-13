from django.urls import path
from .views import CustomAuthToken

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    #path("create_user/", CreatUserView.as_view()),
]