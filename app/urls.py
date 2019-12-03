from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import os
from dotenv import load_dotenv
from rest_framework_swagger.views import get_swagger_view


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=BASE_DIR)


schema_view = get_swagger_view(title='Celery Rest Service')

urlpatterns = [
    url(r'^', include('api.urls')),
    path(str(os.getenv('DJANGO_ADMIN_URL'))+"/", admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-docs', schema_view),
    url(r'^health_check/', include('health_check.urls'))
]