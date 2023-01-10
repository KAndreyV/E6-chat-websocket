from django.shortcuts import render
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView, )
from .models import Writer, Room, Message
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .serializers import *
from rest_framework import viewsets, generics


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


class WritersList(ListView):
    model = Writer
    template_name = 'users.html'
    context_object_name = 'users'
    paginate_by = 10


class WriterDetail(DetailView):
    model = Writer
    template_name = 'user.html'
    context_object_name = 'user'


class WriterUpgrade(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('chat.change_writer',)
    form_class = WriterForm
    model = Writer
    template_name = 'writer_edit.html'
    context_object_name = 'writer'


class RoomList(generics.ListCreateAPIView, LoginRequiredMixin):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView, LoginRequiredMixin):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
