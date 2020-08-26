from django.views.generic import ListView
from django.shortcuts import render

from rest_framework import viewsets

from projects.models import Waiter, Project
from projects.serializers import WaiterSerializer


class WaiterViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer


class ProjectStatusView(ListView):
    waiter = "NONO"
    template_name = 'base.html'
    context_object_name = 'waiter'

    # def get_context_data(self, **kwargs):
    #     """
    #         Add other things to the context
    #     """
    #     context = super(ProjectStatusView, self).get_context_data(**kwargs)
    #     context['project'] = Project.objects.all()
    #     return context

    def get_queryset(self):
        projects = Project.objects.filter(url=self.kwargs["title"])
        return projects
