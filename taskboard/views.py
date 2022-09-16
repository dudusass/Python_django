from django.shortcuts import render
from .models import Board, Task
from .serializer import BoardSerializer, TaskSerializer
from rest_framework import viewsets

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer    


""" def index(request):
    return render(request, "index.html")

def carrinho(request):
    return render(request, "carrinho.html")    

def contato(request):
    return render(request, "contato.html")      
 """