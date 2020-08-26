from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from rest_framework import viewsets

from projects.models import Waiter, Project
from projects.serializers import WaiterSerializer


class WaiterViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer


class ProjectStatusView(PermissionRequiredMixin, ListView):
    permission_required = 'users.is_admin'
    template_name = 'projects/project_status.html'
    context_object_name = 'waiters'

    def get_context_data(self, **kwargs):
        """
            Add other things to the context
        """
        context = super(ProjectStatusView, self).get_context_data(**kwargs)
        project = Project.objects.get(url=self.kwargs["title"])
        waiters = Waiter.objects.filter(project=project)
        context['numberofwaiters'] = len(waiters)
        context['project'] = project
        return context

    def get_queryset(self):
        project = Project.objects.get(url=self.kwargs["title"])
        waiters = Waiter.objects.filter(project=project)
        return waiters
