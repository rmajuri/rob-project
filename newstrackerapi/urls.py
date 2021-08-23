from django.urls import include, path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('api/articles/', views.ArticleView.as_view()),
    path('api/articles/<int:pk>/', views.ArticleView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', views.FrontendAppView.as_view())
]
