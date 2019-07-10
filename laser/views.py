from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils.text import slugify

from . import models


class IndexView(TemplateView):
    template_name = 'laser/index.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'name' in request.GET:
            e = models.EntryLaser(user=request.user, fet=request.GET['name'], navigo=('navigo' in request.GET))
            e.save()
        if request.user.is_authenticated:
            context['last'] = models.EntryLaser.objects.filter(user=request.user).order_by('-time').first()
        return render(request, self.template_name, context)


class SummaryView(TemplateView):
    template_name = 'laser/summary.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summary'] = []
        for user in models.EntryLaser.objects.values('user').distinct():
            e = models.EntryLaser.objects.filter(user=user['user']).order_by('-time').first()
            context['summary'].append(e)
        return render(request, self.template_name, context)
