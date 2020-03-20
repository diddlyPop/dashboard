from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("profile/", views.profile, name="profile"),
    # example of login_required decorator for class based views
    # normally login_required decorator will go above the function view
    path("register/", views.register, name="register"),
]
