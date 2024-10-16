from django.views.generic import DetailView, ListView

from courses.models import Speaker, Drug, Tag, Course
from modules.models import ModuleProgress

__all__ = (
    'IndexView', 'SpeakerDetailView', 'DetailView', 'TagListView', 'TagDetailView', 'CourseDetailView',
    'CertificateDetailView'
)


# Create your views here.
class IndexView(ListView):
    model = Course


class SpeakerDetailView(DetailView):
    model = Speaker


class DrugDetailView(DetailView):
    model = Drug


class TagListView(ListView):
    model = Tag


class TagDetailView(DetailView):
    model = Tag


class CourseDetailView(DetailView):
    model = Course


class CertificateDetailView(DetailView):
    model = Course
    template_name = 'courses/certificate_detail.html'

    # def get(self, request, *args, **kwargs): ... # return generated pdf-file
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_anonymous:
            context['certificated'] = False
            context['error_message'] = 'Login required.'
            return context
        course = self.get_object()
        modules = course.modules.all()
        certificated = all(
            ModuleProgress.objects.filter(
                user=user, module=module,
                video_watched=True, files_downloaded=True, test_passed=True
            ).exists()
            for module in modules
        )
        if not certificated:
            context['error_message'] = 'You must complete all modules to download the certificate.'
        context['certificated'] = certificated
        return context
