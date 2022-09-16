from django.shortcuts import render
from .models import Board, Task
from .serializer import BoardSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer    

    @action(detail=False)
    def pending(self, request):
        queryset = Task.objects.all().filter(status="Pending")
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)