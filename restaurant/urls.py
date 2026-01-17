from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('booking/', views.BookingView, name="Booking"),
    path('menu/', views.MenuItemsView.as_view()),
    path('login/', obtain_auth_token),
]