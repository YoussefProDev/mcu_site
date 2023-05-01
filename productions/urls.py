from django.urls import path
from . import views

app_name = "productions"
urlpatterns = [
    path('', views.ProductionsList.as_view() ,name="ProductionsList"),
    path('<slug:slug>/', views.ProductionsDetail.as_view() ,name="ProductionsDetail"),
]
