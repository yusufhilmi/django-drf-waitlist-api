from django.contrib import admin
from projects.models import Project, Waiter


class WaiterInline(admin.TabularInline):
    model = Waiter
    readonly_fields = ('name', 'email', 'message',)
    fields = ('name', 'email', 'message',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [WaiterInline]
    list_display = ('title', 'waiters')

    def waiters(self, obj):
        return str(len(obj.project.all()))

admin.site.register(Waiter)
