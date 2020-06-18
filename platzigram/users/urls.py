""" User URLs. """

#Django
from django.urls import path
from django.views.generic import TemplateView
from users import views

urlpatterns = [
    

    #Managment
    path(
        route='login/', 
        view=views.login_view, 
        name='login'),
    path(
        route='logout/', 
        view=views.logout_view, 
        name='logout'),
    path(
        route='signup/', 
        view=views.signup, 
        name='signup'),
    path(
        route='me/profile/', 
        view=views.update_profile, 
        name='update_profile'),
    
    
    #Posts
    
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),    
]
