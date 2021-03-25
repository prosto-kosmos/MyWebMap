from django.shortcuts import render

from .forms import AuthUserForm, RegisterUserForm
from .models import Data
from django.views.generic import CreateView, TemplateView, View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    context = {}
    template = 'index.html'
    return render(request,template,context)

class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('map_page')
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('map_page')
    success_msg = 'Пользователь успешно создан'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid

class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('index_url')

class MapView(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = 'next'

    def get(self, request):
        user_data = Data.objects.filter(user = request.user)
        if len(user_data)==0:
            pass
        user_data = user_data[0]
        zoom, e, n = user_data.zoom, user_data.position_e, user_data.position_n
        context = {
            'zoom': zoom,
            'position_e': e,
            'position_n': n,
        }
        template = 'map_page.html'
        return render(request,template,context)
