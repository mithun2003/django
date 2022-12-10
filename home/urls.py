from django.urls import path
from . import views
urlpatterns = [
    path('',views.loginPage,name='login'),      
    path('register',views.registerPage,name='register'),      
    path('logout/',views.logoutUser,name='logout'),      
    path('home',views.index,name='home'),      
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('post',views.post,name='post'),
]
