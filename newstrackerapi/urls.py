from django.urls import include, path
from rest_framework import routers
from .import views

# router = routers.DefaultRouter()
# router.register(r'articles', views.ArticleViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    path('articles/', views.ArticleView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

