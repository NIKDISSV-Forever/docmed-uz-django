from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from docmed.views import NotimplementedView, IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('courses/', include('courses.urls'), name='education'),

    *[path(f'{name}/', NotimplementedView.as_view(), name=name) for name in ['events',
                                                                             'media',
                                                                             'community',
                                                                             'medication',
                                                                             'settings',
                                                                             'logout']],

]

if settings.DEBUG:
    # add media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
