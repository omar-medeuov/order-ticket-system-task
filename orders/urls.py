from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import OrderListView, OrderDetailView, UserRegistrationView, TicketListView, TicketDetailView, \
    TicketUpdateView

urlpatterns = [

    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("api-token-auth/", obtain_auth_token),

    path("tickets/", TicketListView.as_view(), name="ticket_list"),
    path("tickets/<int:pk>/", TicketDetailView.as_view(), name="ticket_detail"),
    path("tickets/<int:pk>/update", TicketUpdateView.as_view(), name="ticket_update"),
    path("<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("", OrderListView.as_view(), name="order_list"),

]