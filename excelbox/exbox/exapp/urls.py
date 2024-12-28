from django.urls import path, include
from .views import authView, home, totalsolutions, additem, success

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("totalsales/", totalsolutions, name="totalsolutions"),
    path("additem/", additem, name="additem"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("success/", success, name="success"),
]