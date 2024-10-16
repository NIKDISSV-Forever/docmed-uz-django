from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'


class NotimplementedView(TemplateView):
    template_name = 'notimplemented.html'
