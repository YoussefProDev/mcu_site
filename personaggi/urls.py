from django.urls import path
from . import views
urlpatterns = [
    path('', views.PersonaggiList.as_view() ,name="PersonaggiList"),
    path('<slug:slug>/', views.PersonaggiDetail.as_view() ,name="PersonaggiDetail"),
]
