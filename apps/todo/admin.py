from django.contrib import admin

from apps.todo.models import ToDo

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'created_at']
    search_fields = ['user__username', 'title', 'description', 'created_at']