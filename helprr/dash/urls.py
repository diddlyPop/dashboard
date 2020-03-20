from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.home, name="home"),
    path("dash/", views.dash, name='dash')
    # example of login_required decorator for class based views
    # normally login_required decorator will go above the function view
]
