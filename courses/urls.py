from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from courses import views, api

app_name = 'courses'

router = DefaultRouter()
router.register(r'tags', api.TagViewSet)
router.register(r'speakers', api.SpeakerViewSet)
router.register(r'drugs', api.DrugViewSet)
router.register(r'courses', api.CourseViewSet)
router.register(r'attaches', api.AttachViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('<int:pk>/certificate/', views.CertificateDetailView.as_view(), name='certificate_detail'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('tag/<int:pk>/', views.TagDetailView.as_view(), name='tag'),
    path('speaker/<int:pk>/', views.SpeakerDetailView.as_view(), name='speaker_detail'),
    path('drug/<int:pk>/', views.DrugDetailView.as_view(), name='drug_detail'),

    path('modules/', include('modules.urls'), name='modules'),

    path('api/', include(router.urls)),
]
