from asyncio import Task
from django.contrib import admin
from .models import Board, Tasks

admin.site.register(Board)
admin.site.register(Tasks)
