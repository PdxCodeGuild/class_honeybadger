from django.contrib import admin

from .models import TodoItem, TodoItemType

admin.site.register(TodoItem)
admin.site.register(TodoItemType)
