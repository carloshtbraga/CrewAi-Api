# admin.py

from django.contrib import admin
from .models import Agent, Task, Crew, Llm

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('role', 'llm', 'verbose', 'memory', 'created_at')
    list_filter = ('verbose', 'memory', 'llm', 'created_at')
    search_fields = ('role', 'goal', 'backstory')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    autocomplete_fields = ('llm',)
    readonly_fields = ('created_at',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description_short', 'agent', 'async_execution', 'created_at')
    list_filter = ('async_execution', 'created_at', 'agent')
    search_fields = ('description', 'expected_output', 'output_file')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    autocomplete_fields = ('agent',)
    readonly_fields = ('created_at',)

    def description_short(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_short.short_description = 'Description'

@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ('id', 'process', 'created_at')
    list_filter = ('process', 'created_at')
    search_fields = ('process',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    filter_horizontal = ('agents', 'tasks')
    readonly_fields = ('created_at',)

@admin.register(Llm)
class LlmAdmin(admin.ModelAdmin):
    list_display = ('model', 'verbose', 'temperature')
    list_filter = ('verbose',)
    search_fields = ('model',)
    ordering = ('model',)
