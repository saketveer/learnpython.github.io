
from django.urls import path
from.import views


urlpatterns = [

    path('register', views.register, name='register'),  # it is used to register page.
    path('signup', views.signup, name='signup'),


]