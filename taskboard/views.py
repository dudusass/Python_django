from django.shortcuts import render
from .models import Board, Task
from .serializer import BoardSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

def index(request):

    context = {
        'minha_chave': Board.objects.all()
    }

    return render(request, 'index.html', context)

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
    
    @action(detail=False)
    def pending(self, request):
        queryset = Task.objects.all().filter(status="Doing")
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False)
    def pending(self, request):
        queryset = Task.objects.all().filter(status="Done")
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)