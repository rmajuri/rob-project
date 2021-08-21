from django.urls import include, path
from . import views

urlpatterns = [
    path('articles/', views.ArticleView.as_view()),
    path('articles/<int:pk>/', views.ArticleView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

