from django.urls import path, include
from rest_framework.routers import DefaultRouter

from modules import views, api

app_name = 'modules'

router = DefaultRouter()
router.register(r'list', api.ModuleViewSet)
router.register(r'timecodes', api.TimecodeViewSet)
router.register(r'progress', api.ModuleProgressViewSet)
router.register('sponsors', api.SponsorViewSet)

urlpatterns = [
    path('', views.ModuleListView.as_view(), name='list'),
    path('certificate/<int:pk>/', views.CertificateDetailView.as_view(), name='certificate'),
    path('<int:pk>/', views.ModuleDetailView.as_view(), name='detail'),
    path('api/', include(router.urls)),
]
