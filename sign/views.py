from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from chat.models import Writer
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


class BaseRegisterView(CreateView):
    model = Writer
    form_class = BaseRegisterForm
    success_url = '/'

#Автоматическое добавление пользователя в группу common
    def post(self, request, *args, **kwargs):
        pass
        form = BaseRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()

            user_group = Group.objects.get(name='common')

            user.groups.add(user_group)

            return redirect('http://127.0.0.1:8000/sign/login/')
        else:
             return render(request, self.template_name, {'form': form})
