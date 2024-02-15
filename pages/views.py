from django.views.generic import TemplateView
from reading_log.models import ReadingLog


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
