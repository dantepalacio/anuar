from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks':tasks})

def terms(request):
    return render(request, 'main/terms.html')

def messenger(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message(
                sender=form.cleaned_data['sender'],
                recipient=form.cleaned_data['recipient'],
                text=form.cleaned_data['text']
            )
            message.save()
            return redirect('messenger')
    else:
        form = MessageForm()
    messages = Message.objects.all()
    sent_messages = messages.filter(sender=request.user.username)
    received_messages = messages.exclude(sender=request.user.username)
    return render(request, 'main/messenger.html', {'sent_messages': sent_messages, 'received_messages': received_messages, 'form': form})


class ProjectLogin(LoginView):
    template_name = '../templates/main/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    template_name = '../templates/main/reg.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class ProjectLogout(LogoutView):
    next_page = reverse_lazy('index')