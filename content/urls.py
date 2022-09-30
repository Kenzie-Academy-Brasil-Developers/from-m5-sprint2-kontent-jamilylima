from django.urls import path
from . import views

urlpatterns = [
    path("content/", views.ContentView.as_view()),
    path("content/<int:content_id>/",views.ContentDetailView.as_view()),
    path("content/filter/",views.ContentfilterView.as_view()),
    
]