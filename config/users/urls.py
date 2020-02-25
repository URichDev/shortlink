from django.urls import path, include

from .views import ProfileView

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name="profile"),
]