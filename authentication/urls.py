from authentication.views import profile,ProfileUpdate

from django.urls import path

app_name = 'authentication'

urlpatterns = [
    path('',profile,name = 'profile'),
    path('update/<slug:slug>/',ProfileUpdate.as_view(),name = 'update'),
]