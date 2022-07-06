from os import path

from django.urls import include


urlpatterns = [
 path('api-auth/', include('rest_framework.urls'))
]