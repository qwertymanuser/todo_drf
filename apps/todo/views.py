from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from apps.todo.models import ToDo
from apps.todo.serializer import ToDoSerializer

# Create your views here.
class ToDoAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin, 
                     CreateModelMixin, 
                     UpdateModelMixin, 
                     DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class ToDoAllDeleteAPIViewSet(DestroyAPIView):
    queryset = ToDo.objects.all()
    
    def delete(self, request, *args, **kwargs):
        todo = ToDo.objects.filter(user=request.user)
        todo = [t for t in todo.delete()]
        return Response({'delete' : 'Все задания удалены'})