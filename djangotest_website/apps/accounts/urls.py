
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name='accounts'
urlpatterns = [
    path("accounts/profile", views.ProfileView.as_view(), name="profile"),
    # Django Auth
    path(
        "login",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("accounts/logout", auth_views.LogoutView.as_view(), name="logout"),
]
