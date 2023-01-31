from django.urls import path
from main.views import *

urlpatterns = [
    path('',HomeView,name='home'),
    path('api/documentation/',DocsView,name='docs'),      
    path('api/messages/',MessageList.as_view(),name='message'),
    path('api/users/',UserList.as_view(),name='user'),
]
