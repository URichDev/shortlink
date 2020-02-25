from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'link_shortener'

urlpatterns = [
    path('', views.LinkShortenerView.as_view()),
    path('my_links', views.ShortLinkList.as_view(), name='links'),
    path('<slug:pk>/update/', views.ShortLinkUpdate.as_view(), name='update'),
    path('<slug:pk>/delete/', views.ShortLinkDelete.as_view(), name='delete'),
]