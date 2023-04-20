from django.urls import path,include
from API.views import CompanyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)


urlpatterns = [
    path('',  include(router.urls)),
]
