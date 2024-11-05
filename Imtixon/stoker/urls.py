from drf_yasg import openapi
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from django.urls import path, re_path, include
from .views import ServiseViewSet, ClientViewSet, AdvisersViewSet, FeaturesViewSet, FAQsViewSet, CommentsViewSet

router = routers.DefaultRouter()
router.register(r'Servises', ServiseViewSet, basename='Servises')
router.register(r'Clients', ClientViewSet, basename='Clients')
router.register(r'Advisers', AdvisersViewSet, basename='Advisers')
router.register(r'Features', FeaturesViewSet, basename='Features')
router.register(r'FAQs', FAQsViewSet, basename='FAQs')
router.register(r'Comments', CommentsViewSet, basename='Comments')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
