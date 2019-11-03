from django.urls import path
from .views import (
                detail,
                login_user_form,
                logout_user,
                sug,
                contact,
                delete,
                about,
                cat,
                
)

app_name = 'BlogStop'

urlpatterns = [
    path('about',about,name='about'),
    path('sug',sug,name='sug'),
    path('login',login_user_form,name='login'),
    path('logout',logout_user,name='logout'),
    path('contact',contact,name='contact'),
    path('<str:slug>',detail),
    path('<str:slug>/cat',cat),
    path('<str:slug>/delete',delete,name='delete'),
    
    #path('<str:slug>/update',update),
    
]
