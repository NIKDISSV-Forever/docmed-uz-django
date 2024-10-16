from django.views.generic import DetailView, ListView

from modules.models import Module, ModuleProgress


class ModuleDetailView(DetailView):
    model = Module

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            module_progress, _ = ModuleProgress.objects.get_or_create(module=self.object, user=user)
            context['module_progress'] = module_progress
        return context


class ModuleListView(ListView):
    model = Module

    def get_queryset(self):
        # Filter the modules to show only those that are not part of a course
        return Module.objects.filter(part_of_course=False)


class CertificateDetailView(DetailView):
    model = Module
    template_name = 'modules/certificate_detail.html'

    # def get(self, request, *args, **kwargs): ... # return generated pdf-file
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_anonymous:
            context['certificated'] = False
            context['error_message'] = 'Login required.'
            return context
        module = self.get_object()
        certificated = ModuleProgress.objects.filter(
            user=user, module=module,
            video_watched=True, files_downloaded=True, test_passed=True
        ).exists()
        if not certificated:
            context['error_message'] = 'You must complete all tasks to download the certificate.'
        context['certificated'] = certificated
        return context
