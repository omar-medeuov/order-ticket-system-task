from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import OrderListView, OrderDetailView, UserRegistrationView

urlpatterns = [

    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("api-token-auth/", obtain_auth_token),
    path("<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("", OrderListView.as_view(), name="order_list"),

]