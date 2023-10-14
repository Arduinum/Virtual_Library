from django.urls import path
from accounts.views import SignInView, CreateUserView, LogoutView


app_name = 'accounts'

urlpatterns = [
    path('login/', SignInView.as_view(), name='sign_in'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
