from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('summary', views.SummaryView.as_view(), name='summary'),
]
