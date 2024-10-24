from django.urls import path
from insta import views
urlpatterns=[
    path('post',views.create,name="createpage"),
     path('home',views.home,name="homepage")
]