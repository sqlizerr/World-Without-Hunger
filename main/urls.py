from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage" ),
    path("index", views.homepage, name="homepage" ),
    path("contact", views.contact, name="contact"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("donatefood", views.donatefood, name="donatefood"),
    path("volunteer_registration", views.volunteer_registration, name="volunteer_registration"),
    path("ngo_registration", views.ngo_registration, name="ngo_registration"),
    path("donatemoney", views.donatemoney, name="donatemoney"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("successpage", views.successpage, name="successpage"),
]