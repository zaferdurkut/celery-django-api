from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views as rest_views


app_name = 'Celery'
router = routers.DefaultRouter()
# router.register(r'customers', views.CustomerList)


urlpatterns = [
    path('', include(router.urls)),
    # url(r'^api-token-auth/', rest_views.obtain_auth_token)
    ]
