### THIS FILE IS NOT BEEN USED AGAIN. I HAVE RESORTED TO ALLAUTH ###

from django.urls import path


from .views import SignupPageView



urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup')
]