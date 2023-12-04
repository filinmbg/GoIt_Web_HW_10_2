from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import LoginForm

app_name = "users"

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="register"), #TODO: check name
    path("signin/", LoginView.as_view(template_name="users/login.html", form_class=LoginForm), name="signin"),
    path("logout/", LoginView.as_view(template_name="users/logout.html"), name="logout"),
]

#

#     path('signin/', LoginView.as_view(template_name="users/signin.html", authentication_form=LoginForm,
#          redirect_authenticated_user=True),name='login'),
