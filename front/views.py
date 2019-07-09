from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils.text import slugify

from . import models


class IndexView(TemplateView):
    template_name = 'front/index.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fets'] = models.Fet.objects.all()
        if 'plat' in request.GET:
            for fet in context['fets']:
                if slugify(str(fet)) == request.GET['plat']:
                    e = models.Entry(user=request.user, fet=fet)
                    e.save()
                    break
        if request.user.is_authenticated:
            context['last'] = models.Entry.objects.filter(user=request.user).order_by('-time').first()
        return render(request, self.template_name, context)


class SummaryView(TemplateView):
    template_name = 'front/summary.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summary'] = []
        context['number'] = {}
        for user in models.Entry.objects.values('user').distinct():
            e = models.Entry.objects.filter(user=user['user']).order_by('-time').first()
            context['summary'].append(e)
            if e.fet in context['number']:
                context['number'][e.fet] += 1
            else:
                context['number'][e.fet] = 1
        return render(request, self.template_name, context)
