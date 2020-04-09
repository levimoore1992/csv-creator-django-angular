from django.urls import path
from .views import CVGenerator
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path('api/cvgenerator', CVGenerator.as_view(), name='cvgenerator')
]