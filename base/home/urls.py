from django.urls import path

from base.home.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
