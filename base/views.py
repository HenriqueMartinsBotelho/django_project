from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class TestView(TemplateView):
    template_name = "base/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About"
        return context