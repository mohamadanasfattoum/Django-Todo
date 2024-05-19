from rest_framework import generics
from .serializers import TodoSerializers
from .models import Todo


class TodoListApi(generics.ListCreateAPIView):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()


class TodoDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializers
    queryset = Todo.objects.all()