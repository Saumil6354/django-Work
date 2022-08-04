from django.urls import path
from . import views

urlpatterns=[
    path('base/',views.base,name='base'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('',views.index,name='index'),
    path('post/',views.post,name='post-details'),
    path('login/',views.login,name='login'),
    path('addblog/',views.addblog,name='addblog'),
    path('<slug:slug>/alltags',views.alltags,name='alltags')
]