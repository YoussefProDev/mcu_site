from django.urls import path
from . import views

app_name = "personaggi"
urlpatterns = [
    path('', views.PersonaggiList.as_view() ,name="PersonaggiList"),
    path('<slug:slug>/', views.PersonaggiDetail.as_view() ,name="PersonaggiDetail"),
]
