# accounts/urls.py
from django.urls import path
from .views import login_view, dashboard_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),  # Login URL
    path('dashboard/', dashboard_view, name='dashboard'),  # Dashboard URL
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout URL
    path('', login_view, name='login'),  # Set login_view as the default landing page
]
